from socket import *
from select import select

s = socket()
s.bind(('0.0.0.0', 11111))
s.listen(3)

s.setblocking(False)  # 设置非阻塞（避免网络问题）

rlist = [s]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            c.setblocking(False)  # 设置非阻塞
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            wlist.append(r)
            # r.send(b"Received")

    for w in wlist:
        w.send(b"OK")
        wlist.remove(w)

    for x in xlist:
        pass
