import socket
#host = socket.gethostname()
host="127.0.0.1"
port=1000
#udpSvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#•Ouvrir une socket en UDP
#tcpSvr = socket.socket()
#tcpSvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#• Ouvrir une socket en TCP

server_socket = socket.socket()
server_socket.bind(host, port)
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
conn.send(reply.encode())
conn.close()