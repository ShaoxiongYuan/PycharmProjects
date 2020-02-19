from socket import *
import struct

st = struct.Struct("i32sif")
sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(("127.0.0.1", 11111))
f = open("stu_info.txt", "a")
while True:
    data, addr = sockfd.recvfrom(1024)
    stu_data = st.unpack(data)
    ID, name, age, score = stu_data
    if score > 90:
        name = name.decode().strip("\x00")
        s = "%d %s %d %.2f" % (ID, name, age, score)
        f.write(s)
        f.flush()

f.close()
sockfd.close()
