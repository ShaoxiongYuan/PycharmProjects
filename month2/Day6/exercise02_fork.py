import sys
import time
import os

def sum():
    result = 0
    for i in range(9999):
        result += i
    print("result:%.2f万" % (result / 10000))

def write():
    with open("file.txt", "w") as f:
        for i in range(99):
            f.write("Hello World\n")

past = time.time()
# 单进程
# sum()
# write()
# now = time.time()

# 多进程
pid = os.fork()

if pid < 0:
    print("进程创建失败")
elif pid == 0:
    write()
    sys.exit("bye")
else:
    sum()

print("执行时间：",time.time()-past)

