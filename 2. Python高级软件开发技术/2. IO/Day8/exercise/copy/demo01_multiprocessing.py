from time import sleep
import multiprocessing


def fun(sec, name):
    for i in range(3):
        print("I'm %s" % name)
        sleep(sec)


if __name__ == '__main__':
    p = multiprocessing.Process(target=fun, args=(2, "Lily"))
    p.daemon=True
    p.start()
    sleep(1)
