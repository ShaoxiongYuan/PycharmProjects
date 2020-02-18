from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

server_addr = ("127.0.0.1", 11111)

while True:
    word = input("请输入单词：")
    if not word:
        break
    sockfd.sendto(word.encode(), server_addr)
    data, addr = sockfd.recvfrom(1024)
    print(data.decode())

sockfd.close()
