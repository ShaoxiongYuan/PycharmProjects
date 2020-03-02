"""
逻辑处理
"""
from multiprocessing import Process
from socket import *
from dict_db import Database
from time import sleep

db = Database()


def login(c, name, password):
    result = db.login(name, password)
    if result:
        c.send(b"OK")
    else:
        c.send(b"Fail")


def register(c, username, password):
    result = db.register(username, password)
    if result:
        c.send(b"OK")
    else:
        c.send(b"Fail")


def search(c, name, word):
    result = db.search(name, word)
    if result:
        c.send(result.encode())
    else:
        c.send("未找到单词".encode())


def history(c, name):
    result = db.history(name)
    for i in result:
        msg = "用户名：%s,单词：%s,时间：%s" % (i[0], i[1], i[2])
        sleep(0.1)
        c.send(msg.encode())
    sleep(0.1)
    c.send(b"end")


def handle(c):
    db.create_cursor()
    while True:
        data = c.recv(1024).decode().split(" ")
        if not data or data[0] == "E":
            c.close()
            return
        elif data[0] == "L":
            login(c, data[1], data[2])
        elif data[0] == "R":
            register(c, data[1], data[2])
        elif data[0] == "S":
            search(c, data[1], data[2])
        elif data[0] == "H":
            history(c, data[1])


def main():
    s = socket()
    s.bind(("127.0.0.1", 11111))
    s.listen(10)
    # signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        print("Waiting for connect...")
        c, addr = s.accept()
        print("Connected from:", addr)
        p = Process(target=handle, args=(c,))
        p.start()


if __name__ == '__main__':
    main()
