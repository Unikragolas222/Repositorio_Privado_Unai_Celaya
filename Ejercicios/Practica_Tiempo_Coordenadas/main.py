from Funciones_Ubicacion import Ubicacion
from Funciones_clima import Clima
from Beans import InterfazClima

def main():
    interfaz = InterfazClima()
    latitud, longitud = interfaz.solicitar_coordenadas()
    
    if latitud and longitud:
        ubicacion = Ubicacion(latitud, longitud)
        ubicacion.obtener_direccion()

        clima = Clima(latitud, longitud)
        clima.obtener_datos_clima()

        interfaz.mostrar_informacion(ubicacion, clima)

if __name__ == "__main__":
    main()
