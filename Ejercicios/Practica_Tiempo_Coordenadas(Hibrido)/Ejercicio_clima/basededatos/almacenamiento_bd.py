
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')

db_name = "eda"
collection_name = "localizaciones"

def obtener_nombres_bases_de_datos():
 # Obtener una lista de todos los nombres de bases de datos
    all_dbs = client.list_database_names()

    # mostramos todas las bases de datos que hay
    print("Todos los nombres de bases de datos:")
    for db_name in all_dbs:
        print(db_name)

def mostrar_todos_datos_base_de_datos():
    # mostramos los datos de una base de datos
    print("Mostramos los datos de una base de datos prueba-hola")
    db_pruebas = client[db_name][collection_name].find({})
    for x in db_pruebas:
        print(x)

def insertar_una_localizacion(localizacion):
# metemos datos en la base de datos de prueba hola
    client[db_name][collection_name].insert_one(localizacion)

def meter_datos_basedatos():
    # mostramos los datos de una base de datos
    print("Mostramos los datos de una base de datos prueba-hola")
    db_pruebas = client[db_name][collection_name].find({})
    for x in db_pruebas:
        print(x)

def cargar_y_usar_datos():
    print(f"Cargando y utilizando datos de '{db_name}.{collection_name}':")
    documentos = client[db_name][collection_name].find({})
    datos = [doc for doc in documentos]
    print("Datos cargados exitosamente.")
    # Aquí puedes añadir lógica para usar los datos cargados
    return datos

def buscar_codigo_postal (codigo_postal):
    # mostramos los datos de una base de datos mediante el filtro
    print("Mostramos los datos especificos de una base de datos prueba-hola")
    db_pruebas = client[db_name][collection_name].find({"codigo postal":codigo_postal})
    for x in db_pruebas:
        print(x)

def buscar_provincia (provincia):
    # mostramos los datos de una base de datos mediante el filtro
        print("Mostramos los datos especificos de una base de datos prueba-hola")
        db_pruebas = client[db_name][collection_name].find({"provincia":provincia})
        for x in db_pruebas:
            print(x)

def obtener_todas_las_ubicaciones():
    try:
        # Conexión a la base de datos MongoDB
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente[db_name]
        coleccion = db[collection_name]
        
        # Obtener todas las ubicaciones como un diccionario
        ubicaciones = {}
        for doc in coleccion.find():  # Cada documento de la colección
            ubicaciones[doc["_id"]] = {
                "latitud": doc.get("latitud"),
                "longitud": doc.get("longitud"),
            }
        return ubicaciones
    except Exception as e:
        print(f"Error al obtener ubicaciones de la base de datos: {e}")
        return {}
