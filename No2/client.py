import socket

# objek socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# alamat IP dan port server
server_ip = '127.0.0.1'
port = 12345

# Terhubung ke server
client_socket.connect((server_ip, port))

# Kirim pesan ke server
message = "Halo, ini pesan dari client!"
client_socket.send(message.encode('utf-8'))

# Terima respons dari server
response = client_socket.recv(1024)
print(f"Respon dari server: {response.decode('utf-8')}")

# Tutup koneksi dengan server
client_socket.close()

