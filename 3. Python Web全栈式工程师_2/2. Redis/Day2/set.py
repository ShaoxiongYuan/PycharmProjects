import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.sadd('pys1', 'a', 'b', 'c', 'd', 'e', 'f')

# print(r.smembers('pys1'))
# print(r.spop('pys1'))
r.sadd('pys2', 'c', 'd', 'e')
print(r.sinter('pys1', 'pys2'))
