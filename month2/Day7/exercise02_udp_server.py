from socket import *

server_addr = ("127.0.0.1", 11111)

user = {}


def login(s, name, addr):
    if name in user:
        s.sendto(b"FAIL", addr)
        return
    else:
        s.sendto(b"OK", addr)

    msg = "\nWelcome %s to the chat room" % name
    for value in user.values():
        s.sendto(msg.encode(), value)
    user[name] = addr


def chat(s, name, content):
    msg = "\n%s: %s" % (name, content)
    for i in user:
        if user[i] != name:
            s.sendto(msg.encode(), user[i])


def quit_chat(s, name):
    msg = "\n%s退出了聊天室" % name
    for i in user:
        if user[i] != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b"EXIT",user[i])
    del user[name]


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(server_addr)

    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(" ", 2)
        if tmp[0] == "L":
            login(s, tmp[1], addr)
        elif tmp[0] == "C":
            chat(s, tmp[1], tmp[-1])
        elif tmp[0] == "Q":
            quit_chat(s, tmp[1])


if __name__ == '__main__':
    main()
