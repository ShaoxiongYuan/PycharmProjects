"""
httpserver 2.0
io多路服用，类封装练习
"""

from socket import *
from select import *

# 具体功能实现
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.dir = dir
        # 多路服用监控列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()  # 套接字属性
        self.sockfd.setblocking(False)
        self.sockfd.bind(self.address)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d"%self.port)
        # 使用IO多路服用处理客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs,ws,xs = select(self.rlist,
                              self.wlist,
                              self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c,addr = r.accept()
                    c.setblocking(False)
                    self.rlist.append(c) # 增加监控对象
                else:
                    # 浏览器发送http请求
                    self.handle(r)

    # 处理客户端具体请求
    def handle(self,connfd):
        request = connfd.recv(4096) # 接收http请求

        # 防止客户端退出data等于空
        if not request:
            self.rlist.remove(connfd) # 移除监控
            connfd.close()
            return

        info = request.decode().split(' ')[1]
        print("请求内容：", info)

        # 请求主页
        if info == '/':
            info = '/index.html'

        try:
            f = open(self.dir+info)
        except:
            data = "HTTP/1.1 404 Not Found\r\n"
            data += "Content-Type:text/html\r\n"
            data += "\r\n"
            data += "Sorry...."
        else:
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type:text/html\r\n"
            data += "\r\n"
            data += f.read() # 网页内容
            f.close()
        connfd.send(data.encode())



if __name__ == '__main__':
    """
    希望通过使用这个类，可以快速搭建一个服务，展示我的网页
    """
    # 用户自己决定的内容
    HOST = '0.0.0.0'
    PORT = 8888
    DIR = "./static"
    # 实例化对象 --》 对象调用方法实现具体功能
    httpd = HTTPServer(HOST,PORT,DIR)
    httpd.serve_forever() # 启动服务