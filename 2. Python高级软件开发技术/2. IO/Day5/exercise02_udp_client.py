from socket import *
import struct

st = struct.Struct("i32sif")
server_addr = ("127.0.0.1", 11111)
sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    print("****************************")
    ID = int(input("输入学生ID："))
    name = input("输入学生姓名：").encode()
    age = int(input("输入学生年龄："))
    score = float(input("输入学生分数："))
    data = st.pack(ID, name, age, score)
    sockfd.sendto(data, server_addr)

sockfd.close()
