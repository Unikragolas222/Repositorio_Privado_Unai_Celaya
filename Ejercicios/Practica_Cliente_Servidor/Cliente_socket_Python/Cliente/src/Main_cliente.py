from Funciones_cliente import iniciar_cliente

if __name__ == "__main__":

    host=input ("Introduce el HOST: ")
    port=input ("Introduce el PORT: ")
    port=int(port)

    iniciar_cliente(host,port)
