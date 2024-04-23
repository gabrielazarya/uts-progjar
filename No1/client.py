import socket
import ssl

HOST = 'localhost'
PORT = 12345

context = ssl.create_default_context()
context.check_hostname = False  # Menonaktifkan verifikasi nama host
context.verify_mode = ssl.CERT_NONE  # Menonaktifkan verifikasi sertifikat

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssl_socket:
        print("Connected to server.")
        while True:
            message = input('Your message: ')
            ssl_socket.sendall(message.encode())
            data = ssl_socket.recv(1024)
            print('Received:', data.decode())
