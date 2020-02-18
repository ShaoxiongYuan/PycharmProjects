import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

sockfd.bind(("127.0.0.1", 11111))

sockfd.listen(100)

print("Waiting for connect...")
connfd, addr = sockfd.accept()
print("Connected from:", addr)

while True:
    data = connfd.recv(1024)
    if data == b"##":
        break
    print("Recv:", data.decode())
    n = connfd.send(b"Thanks")
    print("Send %d bytes" % n)

connfd.close()
sockfd.close()
