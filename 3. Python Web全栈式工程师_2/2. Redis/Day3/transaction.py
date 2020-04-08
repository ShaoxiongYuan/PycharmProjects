import redis

pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379)
r = redis.Redis(connection_pool=pool)

with r.pipeline(transaction=True) as pipe:
    pipe.multi()
    pipe.incr("books")
    pipe.incr("books")
    values = pipe.execute()
