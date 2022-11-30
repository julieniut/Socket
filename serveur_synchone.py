import socket , platform, psutil, os

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

while message !="kill":
    #Réception des messages
    msg = conn.recv(1024)
    message= msg.decode()
    print(message)


    #traitement des Messages
    if message == "CPU":
        print(f"Processor: {platform.processor()}")
        conn.send(platform.processor().encode() )

    if message == "CPU%":
        print(f"cpu pourcent {psutil.cpu_percent()}")
        test=str(f"cpu {psutil.cpu_percent(4)} %")
        conn.send(test.encode())

    if message == "IP":
        print(server_socket.getsockname()[0])
        test=str(f"IP {server_socket.getsockname()[0]} ")
        conn.send( test.encode())

    if message == "RAM":
        print(f"Memory :{psutil.virtual_memory()}")
        test = str(psutil.virtual_memory())
        conn.send(test.encode())

    if message == "OS":
        print(f"System: {platform.platform()}")
        conn.send(platform.platform().encode())

    if message =="Name":
        print(f"Node Name: {platform.node}")
        conn.send(platform.node().encode())

    if message == "pythonV":
        print(f"Processor: {platform.python_version()}")
        conn.send(platform.python_version().encode())

    if message == "DOS:dir":
        commande = os.popen("dir").read()
        print(commande)
        conn.send(commande.encode())

    if message == "disconnet":
        fermeture = "Fermeture de la socket client"
        conn.send(fermeture.encode())
        conn.close()
        print(fermeture)

    if message == "reset":
        conn.close()
        print("Fermeture de la socket client")
        server_socket.close()
        print("Fermeture de la socket server")
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)
        conn, address = server_socket.accept()
        print("Client connecter", {address})

    if message == "DOS: mkdir toto":
        commande = os.system("mkdir toto")
        reply= "dossier toto créer"
        conn.send(reply.encode())

    if message == "Ping":
        commande = os.system("Ping 8.8.8.8")
        if commande==0:
         commande="Ping effectué sans erreur"
         conn.send(commande.encode())
        else:
            commande = "Ping effectué avec erreur"
            conn.send(commande.encode())

    if message == "ping":
        address= "1.1.1.1"
        ping = os.popen(f"ping {address}"). read()
        print(ping)
        conn.send(ping.encode())


    if message == 'connection information':
        hostname = socket.gethostname()
        address = socket.gethostbyname(hostname)
        message = str(f" \n Hostname : {hostname} \n IP: {address}")
        conn.send(message.encode())

    else:
        #j'envoie un message
        reply = "Vérifier la saisie de la commandes \n (Voir DOC) "
        conn.send(reply.encode())
        print("MESSAGE reply envoyer")


conn.close()
print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket server")



