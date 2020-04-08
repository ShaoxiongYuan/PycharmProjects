import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379)
r = redis.Redis(connection_pool=pool)


def double_account(user_id):
    key = 'account_%s' % user_id
    with r.pipeline() as pipe:
        while True:
            try:
                pipe.watch(key)
                value = int(r.get(key))
                value *= 2
                print('value is %s' % value)
                print('sleep start')
                time.sleep(10)
                print('sleep end')
                pipe.multi()
                pipe.set(key, value)
                pipe.execute()
                break
            except redis.WatchError as e:
                print(e)
                continue
    return int(r.get(key))


if __name__ == '__main__':
    print(double_account('steven'))
