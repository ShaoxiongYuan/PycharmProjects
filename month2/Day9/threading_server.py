from socket import *
from threading import Thread

HOST = "127.0.0.1"
PORT = 11111
ADDR = (HOST, PORT)

s = socket()
s.bind(ADDR)
s.listen(3)


def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"OK")


while True:
    print("Waiting for connect...")
    c, addr = s.accept()
    print("Connected from:", addr)

    t = Thread(target=handle, args=(c,))
    t.start()
