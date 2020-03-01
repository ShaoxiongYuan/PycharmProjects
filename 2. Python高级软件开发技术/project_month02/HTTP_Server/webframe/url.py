from socket import *

s = socket()
s.bind(("127.0.0.1", 11111))
s.listen(3)
