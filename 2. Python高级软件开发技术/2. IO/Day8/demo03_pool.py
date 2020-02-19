from multiprocessing import Pool
from time import sleep, ctime


def worker(msg):
    sleep(2)
    print(ctime(), "---", msg)


pool = Pool(10)

for i in range(10):
    msg = "Tedu%d" % i
    pool.apply_async(func=worker, args=(msg,))

pool.close()
pool.join()