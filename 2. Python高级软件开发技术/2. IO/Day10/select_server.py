from socket import *
from select import select

"""
可否同时监控多个客户端和一个监听套接字
有客户端链接 --》 监听套接字
客户端给我发消息 --》 对应的客户端套接字
"""

s = socket()
s.bind(('0.0.0.0', 11111))
s.listen(3)

rlist = [s]

while True:
    rs, ws, xs = select(rlist, [], [])
    if rs[0] == s:
        c, addr = s.accept()
        rlist.append(c)
    else:
        c = rs[0]
        data = c.recv(1024)
        if not data:
            rlist.remove(c)
        print(data.decode())
        c.send(b"Received")
