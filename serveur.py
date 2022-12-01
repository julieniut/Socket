import socket

fichier = "data.txt"
lignes = []
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.rstrip()  # supprime la fin de ligne
        lignes.append(ligne)  # ajoute la ligne à la liste
        #print(ligne)

def serveur():
    msg = ""
    conn = None
    server_socket = None
    while msg != "kill" :
        msg = ""
        server_socket = socket.socket()
        """ options qui permette de réutiliser l'adresse et le port rapidement"""
        #server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        server_socket.bind((ligne, 10010))

        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while msg != "kill" and msg != "reset":
            msg = ""
            try :
                conn, addr = server_socket.accept()
                print (addr)
            except ConnectionError:
                print ("erreur de connection")
                break
            else :
                while msg != "kill" and msg != "reset" and msg != "disconnect":
                    msg = conn.recv(1024).decode()
                    print ("Received from client: ", msg)
                    # msg = input('Enter a message to send: ')
                    """ 
                    le serveur va ici récupere les commandes du client et lui renvoyer. Dans la suite de la SAÉ, 
                    le serveur fera pareil mais en renvoyant le résultat des commandes demandées par le client.
                    """
                    conn.send(msg.encode())
                conn.close()
        print ("Connection closed")
        server_socket.close()
        print ("Server closed")

# Coder les commande ici

if __name__ == '__main__':
    serveur()

