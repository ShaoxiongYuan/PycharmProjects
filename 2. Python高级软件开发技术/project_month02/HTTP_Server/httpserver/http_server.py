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
        request = connfd.recv(4096).decode()
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            data = connect_frame(env)
            if data:
                self.response(connfd, data)

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
        connfd.send(message.encode())


if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.serve_forever()
