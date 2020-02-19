from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

server_addr = ("127.0.0.1", 11111)

while True:
    data = input(">>")
    if not data:
        break
    sockfd.sendto(data.encode(), server_addr)
    data, addr = sockfd.recvfrom(1024)
    print("从：", addr, "接收到：", data.decode())
