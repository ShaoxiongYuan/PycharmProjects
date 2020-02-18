from socket import *

server_addr = ("192.168.0.114", 11111)

sockfd = socket()

sockfd.connect(server_addr)

f = open("1.jpg", "rb")
while True:
    data = f.read(1024)
    sockfd.send(data)
    if not data:
        break
f.close()
sockfd.close()
