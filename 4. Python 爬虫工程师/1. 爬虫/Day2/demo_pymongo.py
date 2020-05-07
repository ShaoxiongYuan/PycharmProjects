import pymongo

# 1.连接对象
conn = pymongo.MongoClient(host='localhost', port=27017)
# 2.库对象
db = conn['maoyandb']
# 3.集合对象
myset = db['maoyanset']

myset.insert_one({
    'name': '肖申克的救赎',
    'star': 'ABC',
    'time': '1970-01-01'
})

myset.insert_many([{}, {}])
