import socket
import threading

clientes = []

# Función para manejar la conexión de cada cliente
def manejar_cliente(conn, addr):
    print(f"[NUEVA CONEXIÓN] {addr} conectado.")
    
    while True:
        try:
            mensaje = conn.recv(1024).decode('utf-8')
            if not mensaje:
                break
            print(f"[{addr}] {mensaje}")
            
            # Enviar el mensaje a los demás clientes
            for cliente in clientes:
                if cliente != conn:
                    cliente.sendall(f"[{addr}] {mensaje}".encode('utf-8'))
        
        except:
            print(f"[DESCONECTADO] {addr} desconectado.")
            clientes.remove(conn)
            break
    
    conn.close()

# Iniciar el servidor
def iniciar_servidor(host,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[ESCUCHANDO] Servidor escuchando en {host}:{port}")
    
    while True:
        conn, addr = server.accept()
        clientes.append(conn)
        thread = threading.Thread(target=manejar_cliente, args=(conn, addr))
        thread.start()
        print(f"[CONEXIONES ACTIVAS] {threading.active_count() - 1}")