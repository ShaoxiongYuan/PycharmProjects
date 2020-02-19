from socket import *
import os
import signal

HOST = "127.0.0.1"
PORT = 11111
ADDR = (HOST, PORT)

location = "/home/tarena/FTP/"


def copy_download(file, dir):
    f = open(location + file, "rb")
    f2 = open(dir + file, "wb")
    while True:
        data = f.read(1024)
        if not data:
            break
        f2.write(data)
    f.close()
    f2.close()


def copy_upload(file, dir):
    f = open(dir + file, "rb")
    f2 = open(location + file, "wb")
    while True:
        data = f.read(1024)
        if not data:
            break
        f2.write(data)
    f.close()
    f2.close()


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            return
        tmp = data.decode().split(" ")
        if tmp[0] == "D":
            download_file(c, tmp[1], tmp[2])
        elif tmp[0] == "U":
            upload_file(c, tmp[1], tmp[2])


def download_file(c, name, loc):
    if not os.path.isdir(loc):
        os.mkdir(loc)
    if loc[-1] != "/":
        loc += "/"
    for file in os.listdir(location):
        if file == name:
            copy_download(file, loc)
    c.send("下载完毕".encode())


def upload_file(c, loc, name):
    if loc[-1] != "/":
        loc += "/"
    try:
        copy_upload(name, loc)
    except:
        c.send("文件上传失败".encode())
    else:
        msg = "文件上传完毕"
        c.send(msg.encode())


def main():
    s = socket()
    s.bind(ADDR)
    s.listen(3)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while True:
        c, addr = s.accept()

        pid = os.fork()

        if pid == 0:
            handle(c)
            os._exit(0)
        else:
            continue


if __name__ == '__main__':
    main()
