# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación

import json
from beans.localizador import Localizador
from basededatos import almacenamiento_bd
from pymongo import MongoClient

class GestorDeDatosClimaticos:

    def __init__(self):
        print("Iniciando gestor de datos climáticos")
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db_name = "eda"
        self.collection_name = "localizaciones"
        self.ubicaciones = self.cargar_ubicaciones()  # Cargar ubicaciones desde la base de datos
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
        return ubicacion_encontrada

    def buscar_por_codigo_postal(self, codigo_postal):
        for ubicacion in self.ubicaciones:
            if ubicacion.codigo_postal == codigo_postal:
                return ubicacion
        return None
    
    def buscar_por_provincia(self, provincia):
        lista_ubicaciones = []
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia == provincia:
                lista_ubicaciones.append(ubicacion)
        return lista_ubicaciones

    def cargar_ubicaciones(self):
        """Cargar ubicaciones desde la base de datos y devolver una lista de instancias de Localizador."""
        ubicaciones = []
        documentos = self.client[self.db_name][self.collection_name].find({})
        for doc in documentos:
            # Usar el método from_dict para crear una instancia de Localizador
            ubicacion = Localizador.from_dict(doc)
            ubicaciones.append(ubicacion)
        return ubicaciones