"""
发起请求，获取结果
"""
from socket import *
import sys


def login(s):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    msg = "L " + username + " " + password
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == "OK":
        print("登录成功")
        second_interface(s, username)
    else:
        print("登录失败")


def second_interface(s, name):
    while True:
        print("""
             1. 查单词     2. 查询历史纪录      3. 注销""")
        choice = input("请输入选项：")
        if choice == "1":
            look_up(s, name)
        elif choice == "2":
            history(s, name)
        elif choice == "3":
            return
        else:
            print("请输入正确选项")


def look_up(s, name):
    while True:
        word = input("请输入单词：")
        if word == "##":
            return
        msg = "S " + name + " " + word
        s.send(msg.encode())
        data = s.recv(1024).decode()
        print(data)


def history(s, name):
    msg = "H " + name
    s.send(msg.encode())
    while True:
        data = s.recv(1024).decode()
        if data == "end":
            break
        print(data)


def register(s):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    msg = "R " + username + " " + password
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == "OK":
        print("注册成功")
    else:
        print("注册失败")


def quit(s):
    s.send(b"E")
    sys.exit("谢谢使用")


def main():
    s = socket()
    s.connect(("127.0.0.1", 11111))
    while True:
        print("""
             ************Welcome************
             1. 登录     2. 注册      3. 退出""")

        choice = input("请输入选项：")
        if choice == "1":
            login(s)
        elif choice == "2":
            register(s)
        elif choice == "3":
            quit(s)
        else:
            print("请输入正确选项")


if __name__ == '__main__':
    main()
