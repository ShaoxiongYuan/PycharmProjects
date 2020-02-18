from time import sleep
import multiprocessing
import os


def th1():
    sleep(2)
    print("吃饭")
    print(os.getppid(), "---", os.getpid())


def th2():
    sleep(3)
    print("睡觉")
    print(os.getppid(), "---", os.getpid())


def th3():
    sleep(4)
    print("打怪")
    print(os.getppid(), "---", os.getpid())


if __name__ == '__main__':
    jobs = []
    for th in [th1, th2, th3]:
        p = multiprocessing.Process(target=th)
        jobs.append(p)
        p.start()

    for i in jobs:
        i.join()
