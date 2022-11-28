import socket , platform, psutil

#host = socket.gethostname()
host="127.0.0.1"
port=10010
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


message="je suis le serveur"

while message !="bye":
    #Réception des messages
    msg = conn.recv(1024)
    message= msg.decode()
    print(message)



    if message == "CPU":
        print(f"Processor: {platform.processor()}")
        conn.send(platform.processor().encode() )

    if message == "CPU%":
        print(f"cpu pourcent {psutil.cpu_percent()}")
        test=str(psutil.cpu_percent(4))
        conn.send(test.encode())


    if message == "pythonV":
        print(f"Processor: {platform.python_version()}")
        conn.send(platform.python_version().encode())

    if message == "arret":
        conn.close()
        print("Fermeture de la socket client")
        server_socket.close()
        print("Fermeture de la socket server")

    #j'envoie un message
    reply = input("Saisir le message: ")
    conn.send(reply.encode())
    print("MESSAGE reply envoyer")

#conn.close()
#print("Fermeture de la socket client")

#server_socket.close()
#print("Fermeture de la socket server"
