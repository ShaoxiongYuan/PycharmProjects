import json
from settings import *
from socket import *
from threading import Thread
from url import *


class WebFrame:
    def __init__(self):
        self.host = FrameHost
        self.port = FramePort
        self.address = (FrameHost, FramePort)
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind(self.address)

    def analyze(self):
        self.sockfd.listen(10)
        while True:
            print("Waiting for connect...")
            c, addr = self.sockfd.accept()
            print("Connected from", addr)
            t = Thread(target=self.handle, args=(c,))
            t.setDaemon(True)
            t.start()

    def handle(self, connfd):
        content = connfd.recv(1024).decode()
        data = json.loads(content)
        if data["info"] == "/":
            data["info"] = "/index.html"
        if data["method"] == "GET":
            if data["info"][-5:] == ".html":
                msg = self.get_html(data["info"])
                response = json.dumps(msg)
                connfd.send(response.encode())
            else:
                msg = self.get_data(data["info"])
                response = json.dumps(msg)
                connfd.send(response.encode())
        elif data["method"] == "POST":
            pass

    def get_html(self, spec):
        try:
            f = open(DIR + spec)
        except:
            with open(DIR + "/404.html") as f:
                return {'status': '404', 'data': f.read()}
        else:
            data = f.read()
            return {'status': '200', 'data': data}

    def get_data(self, spec):
        for name, func in url:
            if spec == name:
                result = func()
                return {'status': '200', 'data': result}
        with open(DIR + "/404.html") as f:
            return {'status': '404', 'data': f.read()}


if __name__ == '__main__':
    w = WebFrame()
    w.analyze()
