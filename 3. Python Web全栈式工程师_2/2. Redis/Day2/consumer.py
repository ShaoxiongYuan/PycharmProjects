import redis
import json

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

while True:
    task = r.brpop('pypc', 5)
    print(task)
    if task:
        json_obj = json.loads(task[1])
        print(json_obj)
