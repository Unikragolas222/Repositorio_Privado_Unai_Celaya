import requests

# Clase Clima para obtener la información del clima
class Clima:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.datos_clima = None

    def obtener_datos_clima(self):
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
            response = requests.get(url)
            self.datos_clima = response.json() if response.status_code == 200 else None
        except Exception as e:
            print(f"Error al obtener los datos del clima: {e}")

    def obtener_resumen_clima(self):
        if self.datos_clima and "current_weather" in self.datos_clima:
            clima_actual = self.datos_clima["current_weather"]
            return {
                "temperatura": clima_actual.get("temperature"),
                "velocidad_viento": clima_actual.get("windspeed"),
                "direccion_viento": clima_actual.get("winddirection")
            }
        else:
            return None



def __init__(self):
