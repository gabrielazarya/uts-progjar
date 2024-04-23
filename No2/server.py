import socket

# objek socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# alamat IP dan port
server_ip = '127.0.0.1'
port = 12345

# Bind socket ke alamat dan port yang ditentukan
server_socket.bind((server_ip, port))

# Mendengarkan koneksi yang masuk
server_socket.listen(5)  # Maksimal 5 koneksi dalam antrian

print(f"Server berjalan di {server_ip}:{port}")

while True:
    # Terima koneksi dari client
    client_socket, client_address = server_socket.accept()

    print(f"Menerima koneksi dari {client_address}")
    
    # Terima data dari client
    data = client_socket.recv(1024)
    if not data:
        break
    
    # Proses data yang diterima
    received_message = data.decode('utf-8')
    print(f"Pesan dari client: {received_message}")
    
    # Kirim balik pesan ke client
    response_message = "Pesan diterima, terima kasih!"
    client_socket.send(response_message.encode('utf-8'))
    
    # Tutup koneksi dengan client
    client_socket.close()

# Tutup socket server
server_socket.close()

