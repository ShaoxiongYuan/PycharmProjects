from socket import *
import os

HOST = "127.0.0.1"
PORT = 11111
ADDR = (HOST, PORT)
location = "/home/tarena/FTP"



def main():
    s = socket()
    s.connect(ADDR)

    while True:
        print("1.上传文件")
        print("2.下载文件")
        print("3.查看文件库")
        print("4.退出")

        choice = input("请选择操作：")
        if choice == "1":
            upload(s)
        elif choice == "2":
            download(s)
        elif choice == "3":
            for i in os.listdir(location):
                print(i)
        elif choice == "4":
            break
    s.close()


def download(s):
    for i in os.listdir(location):
        print(i)
    name = input("输入需要下载的文件：")
    dir2 = input("输入需要下载到的位置：")
    msg = "D " + name + " " + dir2
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())


def upload(s):
    dir = input("输入需要上传的文件位置：")
    name = input("输入需要上传的文件名称：")
    msg = "U " + dir + " " + name
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())


if __name__ == '__main__':
    main()
