from socket import *
from select import *


class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8000, dir=None):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.dir = dir
        self.sockfd = socket()
        self.sockfd.setblocking(False)
        self.sockfd.bind(self.address)
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

    def serve_forever(self):
        self.sockfd.listen(3)
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    c.setblocking(False)
                    self.rlist.append(c)
                else:
                    self.handle(r)

    def handle(self, connfd):
        data = connfd.recv(4096)
        if not data:
            self.rlist.remove(connfd)
            connfd.close()
            return
        self.response(connfd,data)

    def response(self,connfd,data):
        info = data.decode().split(" ")[1]
        if info == "/":
            info = "/index.html"
        try:
            f = open(self.dir + info)
        except:
            data = "HTTP/1.1 404 Not Found\r\n"
            data += "Content-Type:text/html\r\n"
            data += "\r\n"
            data += "Sorry..."
        else:
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type:text/html\r\n"
            data += "\r\n"
            data += f.read()
            f.close()
        connfd.send(data.encode())


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 11111
    DIR = "./static"
    httpd = HTTPServer(HOST, PORT, DIR)
    httpd.serve_forever()
