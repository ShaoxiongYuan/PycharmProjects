from multiprocessing import Process
import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("函数执行时间：", end_time - start_time)
        return res

    return wrapper


list_primes = []
list_processes = []


def find_prime(start, end):
    if start == 1 or start == 2:
        list_primes.append(2)
    for num in range(start, end + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            list_primes.append(num)
    print(sum(list_primes))


@timeit
def processes():
    div_num = int(input(">>"))
    for p in range(div_num):
        process = Process(target=find_prime, args=((100000 // div_num) * p + 1, (100000 // div_num) * (p + 1)))
        list_processes.append(process)
        process.start()
    for i in list_processes:
        i.join()


if __name__ == '__main__':
    processes()
