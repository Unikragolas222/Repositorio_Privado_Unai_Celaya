from geopy.geocoders import Nominatim

# Clase Ubicacion para obtener la dirección
class Ubicacion:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = None

    def obtener_direccion(self):
        try:
            geolocator = Nominatim(user_agent="test")
            location = geolocator.reverse(f"{self.latitud}, {self.longitud}")
            self.direccion = location.raw if location else None
        except Exception as e:
            print(f"Error al obtener la dirección: {e}")
