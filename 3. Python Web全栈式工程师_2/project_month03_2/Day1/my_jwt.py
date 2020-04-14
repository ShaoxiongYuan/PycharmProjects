import base64
import hmac
import time
import json
import copy
import jwt


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(my_payload, key, exp=300):
        header = {'alg': 'HS256', 'typ': 'JWT'}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        header_bs = Jwt.b64encode(header_json.encode())

        payload = copy.deepcopy(my_payload)
        payload['exp'] = time.time() + exp
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())

        h = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        h_bs = Jwt.b64encode(h.digest())

        return header_bs + b'.' + payload_bs + b'.' + h_bs

    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    @staticmethod
    def decode(token, key):
        header_bs, payload_bs, sign_bs = token.split(b'.')

        h = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        if Jwt.b64encode(h.digest()) != sign_bs:
            raise Exception('造假！！！')

        payload_j = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_j)
        exp = payload['exp']
        now = time.time()
        if now > exp:
            raise Exception('过期！！！')

        return payload

    @staticmethod
    def b64decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
        return base64.urlsafe_b64decode(b_s)


if __name__ == '__main__':
    # s1 = Jwt.encode({'username': 'stevenpp'}, 'abcdef')
    s = jwt.encode({'username': 'steven', 'exp': time.time() + 300}, 'abcdef', algorithm='HS256')
    t = jwt.decode(s, 'abcdef', algorithms='HS256')
    print(s)
    # print(len(s1))
    print(t['username'])
