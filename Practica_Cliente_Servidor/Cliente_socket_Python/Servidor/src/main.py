from Funciones_Servidor.Funciones_server import iniciar_servidor

if __name__ == "__main__":

    host=input ("Introduce el HOST: ")
    port=input ("Introduce el PORT: ")
    port=int(port)

    iniciar_servidor(host,port)
