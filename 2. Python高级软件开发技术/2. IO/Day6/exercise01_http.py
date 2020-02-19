from socket import *


def response():
    data1 = c.recv(2048)

    # 防止客户端崩掉，服务器退出
    if not data1:
        return

    info = data1.decode().split(" ")[1]
    print("请求内容：", info)
    if info == "/":
        with open("index.html") as f:
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type:text/html\r\n"
            data += "\r\n"
            data += f.read()
        return data
    else:
        data = "HTTP/1.1 404 Not Found\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += "Sorry. Website not found."
        return data


s = socket()
s.bind(("127.0.0.1", 11111))
s.listen(3)

while True:
    c, addr = s.accept()
    print("连接自：", addr)
    data = response()
    c.send(data.encode())

c.close()
s.close()
