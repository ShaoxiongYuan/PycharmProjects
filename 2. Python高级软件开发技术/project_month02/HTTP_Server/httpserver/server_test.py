from socket import *
import json

s = socket()
s.bind(('127.0.0.1', 8080))
s.listen(3)

c, addr = s.accept()

data = c.recv(1024)
print(data)
data = json.dumps({'status': '200', 'data': 'OKOKOK'})
c.send(data.encode())

c.close()
s.close()
