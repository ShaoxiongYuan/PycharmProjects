from socket import *
from select import *

# 具体功能实现
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.dir = dir
        self.sockfd = socket()  # 套接字属性
        self.sockfd.setblocking(False)
        self.sockfd.bind(self.address)

    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)

        # 使用IO多路服用处理客户端请求
        rlist = [self.sockfd]  # 处理客户端链接
        wlist = []
        xlist = []

        while True:
            print("等待处理IO.....")
            rs, ws, xs = select(rlist, wlist, xlist)

            # 遍历返回值列表，看看是哪个IO就绪了
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connected from", addr)
                    c.setblocking(False)
                    rlist.append(c)
                else:
                    # 如果r遍历到客户端链接套接字说明： 有客户端给我发消息
                    data = r.recv(1024)
                    if not data:
                        rlist.remove(r)
                        r.close()
                        continue
                    print(data.decode())
                    wlist.append(r)

            for w in ws:
                w.send(b'OK')
                wlist.remove(w)



if __name__ == '__main__':
    """
    希望通过使用这个类，可以快速搭建一个服务，展示我的网页
    """
    # 用户自己决定的内容
    HOST = '0.0.0.0'
    PORT = 11111
    DIR = "./static"
    # 实例化对象 --》 对象调用方法实现具体功能
    httpd = HTTPServer(HOST,PORT,DIR)
    httpd.serve_forever() # 启动服务