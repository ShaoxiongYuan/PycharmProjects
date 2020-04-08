import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.zadd('pyz1', {'steven': 8000, 'guoxiaonao': 12000, 'wangweichao': 15000})
r.zadd('pyz2', {'steven': 6000})
# print(r.zrange('pyz1', 0, -1, withscores=True))
r.zinterstore('pyz3', ('pyz1', 'pyz2'), aggregate='max')
print(r.zrange('pyz3', 0, -1, withscores=True))
