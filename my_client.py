import socket


HEADER =64
PORT=5000

SERVER="127.0.0.1" 
ADDR=(SERVER,PORT)
FORMAT='utf-8'

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)



def start_client() :
    try:
        client_socket.connect(ADDR)
        while True :
            message=input("Enter a message (or 'terminate' to exit):")
            client_socket.sendall(message.encode(FORMAT))
            if message.lower()=="terminate":
                break
    finally:
       client_socket.close()


print("[STARTING] client is starting...")
start_client()



