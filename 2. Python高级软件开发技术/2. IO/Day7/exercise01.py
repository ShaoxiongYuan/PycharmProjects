import os
import time


def fun1():
    print("开始第一件事")
    time.sleep(4)
    print("结束第一件事")


def fun2():
    print("开始第二件事")
    time.sleep(3)
    print("结束第二件事")


pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    pid2 = os.fork()
    if pid2 < 0:
        print("error")
    elif pid2 == 0:
        fun2()
    else:
        os._exit(1)
else:
    os.wait()
    fun1()
