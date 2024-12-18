# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
import json
from beans.localizador import Localizador
from basededatos import almacenamiento_bd

class GestorDeDatosClimaticos:
    ubicaciones = []

    def __init__(self):
        print("Iniciando gestor de datos climáticos")
        # TODO: cargar datos de bd
        self.ubicaciones = []  # Inicializa la lista vacía
        self.cargar_latitudes_longitudes()  # Carga ubicaciones desde la base de datos
        print(f"Número de ubicaciones actuales: {self.get_numero_ubicaciones()}")

    def get_numero_ubicaciones(self):
        return len(self.ubicaciones)

    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        provincias_codigos_postales = {}
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia in provincias_codigos_postales:
                provincias_codigos_postales[ubicacion.provincia].append(ubicacion.codigo_postal)
            else:
                provincias_codigos_postales[ubicacion.provincia] = [ubicacion.codigo_postal]
        if provincias_codigos_postales:
            print(json.dumps(provincias_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")

    def insertar_nueva_ubicacion(self, latitud, longitud):
        ubicacion_encontrada = False
        for ubicacion in self.ubicaciones:
            if ubicacion.check_lat_lng(latitud, longitud):
                ubicacion_encontrada = True
                print("================================================")
                print("Ubicación ya existe")
                print(ubicacion.mostrar_informacion())
                print("================================================")
                break
        if not ubicacion_encontrada:
            p = Localizador(latitud, longitud)
            almacenamiento_bd.insertar_una_localizacion(p.to_dict())
            self.ubicaciones.append(p)
            print("Ubicación agregada correctamente")
        else:
            print("Ubicación ya existe")
        return ubicacion_encontrada

    def buscar_por_codigo_postal(self, codigo_postal):
        ubicacion_encontrada = None
        for ubicacion in self.ubicaciones:
            if ubicacion.codigo_postal == codigo_postal:
                ubicacion_encontrada = ubicacion
                break
        return ubicacion_encontrada

    def buscar_por_provincia(self, provincia):
        lista_ubicaciones = []
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia == provincia:
                lista_ubicaciones.append(ubicacion)
        return lista_ubicaciones

    from basededatos.almacenamiento_bd import cargar_y_usar_datos  # Importa la función de base de datos

    def cargar_latitudes_longitudes(self):
        try:
            # Supongamos que "almacenamiento_bd" tiene un método para obtener todas las ubicaciones
            ubicaciones_hash = almacenamiento_bd.obtener_todas_las_ubicaciones()  # Devuelve un diccionario/tabla hash
            for key, value in ubicaciones_hash.items():
            # key puede ser un identificador único (ej. ID), y value debe contener latitud y longitud
                latitud = value.get("latitud")
                longitud = value.get("longitud")
            
                # Crea un objeto Localizador para cada ubicación
                nueva_ubicacion = Localizador(latitud=latitud, longitud=longitud)
                self.ubicaciones.append(nueva_ubicacion)  # Agrega la ubicación a la lista
            
            print(f"{len(ubicaciones_hash)} ubicaciones cargadas desde la base de datos.")
        except Exception as e:
            print(f"Error al cargar ubicaciones desde la base de datos: {e}")