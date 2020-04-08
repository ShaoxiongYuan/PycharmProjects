import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# key_list = r.keys("*")
#
# for key in key_list:
#     print(key.decode())

# print(r.exists('l1'))
#
# r.lpush('pyl1', '1', '2', '3', '4', '5')
# print(r.lrange('pyl1', 0, -1))

# print(r.rpop('pyl1').decode())

# print(r.ltrim('pyp1', 0, 1))

r.set('name', 'steven')
r.mset({'pyusername1': 'steven', 'pyusername2': 'wanglaoshi'})

r.setbit('p2', 3, 1)
r.bitcount('p2')
