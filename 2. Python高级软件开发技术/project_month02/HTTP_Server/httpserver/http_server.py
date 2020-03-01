from socket import *
from config import *
from threading import *
import re


def connect_frame(env):
    pass


class HTTPServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.address = (HOST, PORT)
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind(self.address)

    # 启动服务 多线程并发
    def serve_forever(self):
        self.sockfd.listen(3)
        while True:
            print("Waiting for connect...")
            connfd, addr = self.sockfd.accept()
            print("Connected from", addr)
            t = Thread(target=self.handle,
                       args=(connfd,))
            t.setDaemon(True)
            t.start()

    def handle(self, connfd):
        # 接受HTTP请求
        request = connfd.recv(4096).decode()
        # 给webframe {'method':'GET','info':XX}
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            # 将env 发送给webframe得到数据
            data = connect_frame(env)
            if data:
                self.response(connfd, data)

    # 将数据组织为响应给浏览器发送
    def response(self, connfd, data):
        if data['status'] == '200':
            message = "HTTP/1.1 200 OK\r\n"
            message += "Content-Type:text/html\r\n"
            message += "\r\n"
            message += data['data']
        elif data['status'] == '404':
            message = "HTTP/1.1 404 Not Found\r\n"
            message += "Content-Type:text/html\r\n"
            message += "\r\n"
            message += data['data']
        elif data['status'] == '500':
            message = "HTTP/1.1 500 Server Error\r\n"
            message += "Content-Type:text/html\r\n"
            message += "\r\n"
            message += data['data']
        connfd.send(message.encode())  # 给浏览器


if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.serve_forever()  # 启动服务
