from threading import Thread
import time


# 无参数
def music():
    time.sleep(2)
    print("播放黄河大合唱")


t = Thread(target=music)

t.setDaemon(True)
t.start()

print(t.is_alive())

