import socket
import threading
from Funciones_cliente import iniciar_cliente

def recibir_mensajes(client):
    while True:
        try:
            mensaje = client.recv(1024).decode('utf-8')
            if mensaje:
                print(mensaje)
        except:
            print("Error al recibir el mensaje.")
            client.close()
            break

def enviar_mensajes(cliente):
    while True:
        mensaje = input("")
        cliente.sendall(mensaje.encode('utf-8'))

def iniciar_cliente(host,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Crear hilos para enviar y recibir mensajes simultáneamente
    thread_recibir = threading.Thread(target=recibir_mensajes, args=(client,))
    thread_enviar = threading.Thread(target=enviar_mensajes, args=(client,))

    thread_recibir.start()
    thread_enviar.start()
