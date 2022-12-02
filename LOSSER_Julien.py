import socket
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QLabel
import sys

#https://github.com/julieniut/Socket

class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        arret_thread=True
        super().__init__(parent)
        self.i = 1
        self.setWindowTitle("Chronomètre")
        self.resize(350, 270)
        self.label = QLabel('Compteur :')
        self.textEdit = QTextEdit("0")
        self.textEdit.setEnabled(False)
        self.btnPress1 = QPushButton("Start")
        self.btnPress2 = QPushButton("Reset")
        self.btnPress3 = QPushButton("stop")
        self.btnPress4 = QPushButton("connect")
        self.btnPress5 = QPushButton("Quitter")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.btnPress3)
        layout.addWidget(self.btnPress4)
        layout.addWidget(self.btnPress5)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.start)
        self.btnPress2.clicked.connect(self.Reset)
        self.btnPress3.clicked.connect(self.STOP)
        self.btnPress4.clicked.connect(self.CONNECT)
        self.btnPress5.clicked.connect(self.QUITTER)

    def start(self):
       # while self.btnPress2.clicked.connect(self.start):
            self.textEdit.append(f" {self.i}")
            self.i += 1

       # while arret_thread == False:
        #    self.i += 1
         #   self.textEdit.append(f" {self.i}").threading.Thread(target=start, args=[i])

    def _start(self):
        # self.textEdit.append(f" {self.i}")
        # self.i += 1
        while arret_thread == False:
            self.i += 1
            self.textEdit.append(f" {self.i}")

    def Reset(self):
        self.textEdit.setPlainText("")
        self.i = 0
        message = "Reset"
       # client_socket.send(message.encode())

    def STOP(self):
        #if arret_thread == True:
         self.textEdit.append(f"STOP")
         #threading.Thread.join()
         message = "STOP"
        # client_socket.send(message.encode())




    def CONNECT(self):
        host = "localhost"
        port = 10000

        client_socket = socket.socket()
        client_socket.connect((host, port))
        print("Serveur est connecté")
        message = "je suis le client"
        #client_socket.send(message.encode())
        self.textEdit.append(f"CONNECT")

    def QUITTER(self):
        message = "bye"
        client_socket.send(message.encode())
        QApplication.exit(0)
        #sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())


host="localhost"
port=10000

client_socket = socket.socket()
client_socket.connect((host, port))

message="je suis le client"
print("Serveur est connecté")




while message !="bye":
    message = input("saisir le message ")
    client_socket.send(message.encode())
    print("Message envoyé")

    message = client_socket.recv(1024).decode()
    print(f"Envoyé du serveur, {message}")



