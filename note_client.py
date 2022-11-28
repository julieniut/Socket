import socket

host="127.0.0.1"
port=10000

client_socket = socket.socket()
client_socket.connect((host, port))

print("Serveur est connecté")
message = input()
client_socket.send(message.encode())
print("Message envoyé")

message = client_socket.recv(1024).decode()
print(f"Envoyé du serveur,{message}")

client_socket.close()
