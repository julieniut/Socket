import socket
#host = socket.gethostname()
host="127.0.0.1"
port=10000
#udpSvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Ouvrir une socket en UDP
#tcpSvr = socket.socket()
#tcpSvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Ouvrir une socket en TCP

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print("en attente du client")
conn, address = server_socket.accept()
print("Client connecter",{address})

#Réception des messages
msg = conn.recv(1024)
message= msg.decode()
print(message)

#j'envoie un message
reply = input("Saisir le message: ")
conn.send(reply.encode())
print("MESSAGE reply envoyer")

conn.close()
print("Fermeture de la socket client")

server_socket.close()
print("Fermeture de la socket server")