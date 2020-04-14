import json
import hashlib
import time

import jwt
from django.conf import settings
from django.http import JsonResponse
from user.models import UserProfile


# Create your views here.
def tokens(request):
    if request.method != 'POST':
        return JsonResponse({'code': 10200, 'error': 'Please use POST instead.'})

    json_str = request.body
    data = json.loads(json_str)
    username = data['username']
    password = data['password']
    # TODO 校验参数

    old_users = UserProfile.objects.filter(username=username)
    if not old_users:
        return JsonResponse({'code': 10201, 'error': 'Username or password is wrong.'})

    user = old_users[0]
    m = hashlib.md5()
    m.update(password.encode())
    if user.password != m.hexdigest():
        return JsonResponse({'code': 10202, 'error': 'Username or password is wrong.'})

    token = make_token(username)

    return JsonResponse({'code': 200, 'username': username, 'data': {'token': token.decode()}, 'cart_count': 0})


def make_token(username, exp=3600 * 24):
    now = time.time()
    payload = {'username': username, 'exp': now + exp}
    return jwt.encode(payload, settings.JWT_TOKEN_KEY, algorithm='HS256')
