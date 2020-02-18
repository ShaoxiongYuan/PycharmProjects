import socket

sockfd = socket.socket()

sockfd.bind(("192.168.0.114", 11111))

sockfd.listen(100)

print("Waiting for connect...")
connfd, addr = sockfd.accept()
print("Connected from:", addr)

f = open("1(copy).jpg", "wb+")
while True:
    data = connfd.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
connfd.close()
sockfd.close()
