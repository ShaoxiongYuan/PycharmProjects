from threading import Thread
import time


# 无参数
def music():
    for i in range(3):
        time.sleep(2)
        print("播放黄河大合唱")


# 有参数
def fun(sec, name):
    time.sleep(sec)
    print("%s执行完毕" % name)


jobs = []

for i in range(5):
    thread = Thread(target=fun, args=(2,), kwargs={"name": "T%d" % i})
    thread.start()

for i in jobs:
    i.join()
