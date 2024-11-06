import requests
from geopy.geocoders import Nominatim

# Clase para obtener la dirección a partir de la latitud y longitud usando Nominatim
class Localizador:

    latitud = None

    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = None

    def obtener_direccion(self):
        try:
            geolocator = Nominatim(user_agent="test")
            location = geolocator.reverse(f"{self.latitud}, {self.longitud}")
            self.direccion = location.address if location else "Dirección no encontrada"
        except Exception as e:
            print(f"Error al obtener la dirección: {e}")
            self.direccion = "Error al obtener la dirección"
        return self.direccion


# Clase para obtener el clima (temperatura y velocidad del viento) de Open-Meteo
class Clima:

    latitud = None


    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.temperatura = None
        self.velocidad_viento = None

    def obtener_datos_climaticos(self):
        
        try:
            # URL de la API de Open-Meteo
            url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
            
            # Hacer la solicitud a la API
            response = requests.get(url)
            data = response.json()

            # print("----------------------------------------------------")
            # print(data)
            # print("----------------------------------------------------")


            if response.status_code == 200 and "current_weather" in data:
                current_weather = data["current_weather"]
                self.temperatura = current_weather["temperature"]
                self.velocidad_viento = current_weather["windspeed"]
            else:
                print("Error: No se pudieron obtener los datos climáticos.")
                self.temperatura, self.velocidad_viento = "Desconocido", "Desconocido"
        except Exception as e:
            print(f"Error al obtener los datos climáticos: {e}")
            self.temperatura, self.velocidad_viento = "Error", "Error"
        return self.temperatura, self.velocidad_viento


# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
class GestorDeDatosClimaticos:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.localizador = Localizador(latitud, longitud)
        self.clima = Clima(latitud, longitud)

    def obtener_informacion(self):
        # Obtener la dirección
        direccion = self.localizador.obtener_direccion()
        print(f"Dirección: {direccion}")
        
        # Obtener los datos climáticos
        temperatura, velocidad_viento = self.clima.obtener_datos_climaticos()
        print(f"Temperatura: {temperatura}°C")
        print(f"Velocidad del viento: {velocidad_viento} km/h")

# Ejemplo de uso
if __name__ == "__main__":
    # Coordenadas del usuario
    latitud = input("inserta la latitud ")
    longitud = input("inserta la longitud ")

    # Crear el gestor de datos y obtener la información
    gestor = GestorDeDatosClimaticos(latitud, longitud)
    gestor.obtener_informacion()