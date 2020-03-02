import json
import re
from socket import *
from threading import *
from config import *


def connect_frame(content):
    s = socket()
    s.connect((frame_ip, frame_port))
    try:
        data = json.dumps(content)
        s.send(data.encode())
        result = s.recv(1024 * 1024 * 10).decode()
        return json.loads(result)
    except:
        return


class HTTPServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.address = (HOST, PORT)
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind(self.address)

    def serve(self):
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
        print(request)
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            content = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            data = connect_frame(content)
            if data:
                self.response(connfd, data)

    def response(self, connfd, data):
        if data['status'] == '200':
            message = "HTTP/1.1 200 OK\r\n"
            message += "Content-Type:text/html\r\n"
            message += "\r\n"
            message += data['data']
            connfd.send(message.encode())
        elif data['status'] == '404':
            message = "HTTP/1.1 404 Not Found\r\n"
            message += "Content-Type:text/html\r\n"
            message += "\r\n"
            message += data['data']
            connfd.send(message.encode())
        elif data['status'] == '500':
            message = "HTTP/1.1 500 Server Error\r\n"
            message += "Content-Type:text/html\r\n"
            message += "\r\n"
            message += data['data']
            connfd.send(message.encode())


if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.serve()
