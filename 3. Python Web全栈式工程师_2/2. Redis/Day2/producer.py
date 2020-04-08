import redis
import json

r = redis.Redis(host='127.0.0.1', db=0, port=6379)

json_obj = {'task': 'send_email', 'from': 'steven',
            'to': '2379773801@qq.com', 'content': 'hello'}

json_str = json.dumps(json_obj)

r.lpush('pypc', json_str)
