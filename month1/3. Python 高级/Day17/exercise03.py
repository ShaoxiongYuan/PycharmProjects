import time


def func_time(func):
    def wrapper(*args, **kwargs):
        past = time.time()
        result = func(*args, **kwargs)
        now = time.time()
        print("用了%.20f秒" % (now - past))
        return result

    return wrapper


@func_time
def func01():
    print("func01正在执行...")
    for __ in range(10):
        pass


@func_time
def func02():
    print("func02正在执行...")
    for __ in range(1000000000):
        pass


func01()
func02()
