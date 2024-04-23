import ssl
import socket

certfile_path_1 = 'No1/certs/server.crt'
keyfile_path_1 = 'No1/certs/server.key'

certfile_path_2 = 'certs/server.crt'
keyfile_path_2 = 'certs/server.key'

try:
    with open(certfile_path_1):
        pass
    with open(keyfile_path_1):
        pass
    certfile = certfile_path_1
    keyfile = keyfile_path_1
except FileNotFoundError:
    try:
        with open(certfile_path_2):
            pass
        with open(keyfile_path_2):
            pass
        certfile = certfile_path_2
        keyfile = keyfile_path_2
    except FileNotFoundError:
        raise FileNotFoundError("Sertifikat atau kunci pribadi tidak ditemukan.")

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile, keyfile=keyfile)

HOST = 'localhost'
PORT = 12345

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
