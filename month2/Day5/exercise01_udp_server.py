from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(("127.0.0.1", 11111))

dictionary = open("dict.txt", "r")


def look_up_word():
    while True:
        word, addr = sockfd.recvfrom(1024)
        for line in dictionary:
            if word.decode() == line.split(" ")[0]:
                sockfd.sendto(line.encode(), addr)
                break
            elif word.decode() < line.split(" ")[0]:
                sockfd.sendto("没有该单词".encode(), addr)
                break


look_up_word()
dictionary.close()
sockfd.close()
