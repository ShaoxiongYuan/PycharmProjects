from threading import Thread, Lock

# def spider():
#     print('I am spider man.')
#
#
# jobs = []
#
# for i in range(100):
#     t = Thread(target=spider)
#     jobs.append(t)
#     t.start()
#
# for job in jobs:
#     job.join()

n = 5000
lock = Lock()


def f1():
    global n
    for i in range(1000000):
        lock.acquire()
        n = n + 1
        lock.release()


def f2():
    global n
    for i in range(1000000):
        lock.acquire()
        n = n - 1
        lock.release()


t1 = Thread(target=f1)
t1.start()

t2 = Thread(target=f2)
t2.start()

t1.join()
t2.join()

print(n)
