import os
import sys
from socket import *

server_addr = ("127.0.0.1", 11111)


def receive_message(s):
    while True:
        data, addr = s.recvfrom(1024)
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode() + '\n', end="")


def main():
    # udp 客户端
    s = socket(AF_INET, SOCK_DGRAM)

    while True:
        name = input("请输入姓名：")
        msg = "L " + name
        s.sendto(msg.encode(), server_addr)
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print("该用户已存在")

    while True:
        pid = os.fork()
        if pid < 0:
            print("error")
        elif pid == 0:
            receive_message(s)
        else:
            send_message(name, s)


def send_message(name, s):
    try:
        content = input("发言：")
    except:
        content = ""
    if content == "":
        msg = "Q " + name
        s.sendto(msg.encode(), server_addr)
        sys.exit("谢谢使用")
    msg = "C " + name + " " + content
    s.sendto(msg.encode(), server_addr)


if __name__ == '__main__':
    main()
