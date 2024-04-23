import socket
import ssl

HOST = 'localhost'
PORT = 12345

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='certs/server.crt', keyfile='certs/server.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    with context.wrap_socket(server_socket, server_side=True) as ssl_socket:
        print("Server listening...")
        conn, addr = ssl_socket.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('Received:', data.decode())
                message = input('Your message: ')
                conn.sendall(message.encode())
