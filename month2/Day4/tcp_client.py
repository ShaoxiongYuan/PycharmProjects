from socket import *

server_addr = ("127.0.0.1", 11111)

sockfd = socket()

sockfd.connect(server_addr)

while True:
    data = input(">>")
    sockfd.send(data.encode())
    if data == "##":
        break
    data = sockfd.recv(1024)
    print("from server:", data.decode())

sockfd.close()
