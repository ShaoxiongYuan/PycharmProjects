from socket import *
import os
from signal import *

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


signal(SIGCHLD, SIG_IGN)
while True:
    print("Waiting for connect...")
    c, addr = s.accept()
    print("Coneected from:", addr)
    pid = os.fork()

    if pid == 0:
        handle(c)
        os._exit(0)
    else:
        continue
