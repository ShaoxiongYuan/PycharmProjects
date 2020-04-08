import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', db=1, port=6379)
r = redis.Redis(connection_pool=pool)


def withpipeline(r):
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i + 1
        p.set(key, value)
    p.execute()


def withoutpipeline(r):
    for i in range(1000):
        key = 'test2' + str(i)
        value = i + 1
        r.set(key, value)


if __name__ == '__main__':
    t1 = time.time()
    # 0.04984927177429199
    withpipeline(r)

    # 0.17720866203308105
    # withoutpipeline(r)
    t2 = time.time()
    print(t2 - t1)
