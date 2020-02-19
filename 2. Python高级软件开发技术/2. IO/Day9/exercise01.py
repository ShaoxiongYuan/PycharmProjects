from threading import Thread, Lock


def print_letter():
    for i in range(ord("A"), ord("Z") + 1):
        lock2.acquire()
        print(chr(i), end="")
        lock1.release()


def print_number():
    for i in range(1, 53, 2):
        lock1.acquire()
        print(i, end="")
        print(i + 1, end="")
        lock2.release()


lock1 = Lock()
lock2 = Lock()

lock2.acquire()

t1 = Thread(target=print_number)
t2 = Thread(target=print_letter)

t1.start()
t2.start()

t1.join()
t2.join()
