import socket

host="127.0.0.1"
port=1000

client_socket = socket.socket()
client_socket.connect(host, port)
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
client_socket.close()
