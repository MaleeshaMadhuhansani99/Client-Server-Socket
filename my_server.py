import socket

PORT=5000
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', PORT)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print(f"Server started on port {PORT}")

    connection, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    try:
        while True:
            data = connection.recv(1024).decode()
            if data:
                print(f"Received from client: {data}")
            else:
                break
    finally:
        connection.close()
        print("Server terminated")



print("[STARTING] server is starting...")
start_server()
