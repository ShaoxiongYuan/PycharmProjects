import base64
import hashlib
import json
import random
import requests

from django.db import transaction
from django.http import JsonResponse
from django.core.cache import cache
from django.views import View
from django.conf import settings
from urllib.parse import urlencode

from dtoken.views import make_token
from .tasks import send_active_email_async
from .models import *
from tools.login_decorator import login_check


def users(request):
    if request.method != 'POST':
        return JsonResponse({'code': 10100, 'error': 'Please use POST !'})

    json_str = request.body
    data = json.loads(json_str)
    username = data['uname']
    email = data['email']
    password = data['password']
    phone = data['phone']
    old_users = UserProfile.objects.filter(username=username)
    if old_users:
        result = {'code': 10101, 'error': 'Your username is already existed!'}
        return JsonResponse(result)

    m = hashlib.md5()
    m.update(password.encode())

    try:
        UserProfile.objects.create(username=username, password=m.hexdigest(), email=email, phone=phone)
    except Exception as e:
        print('---create error is ---')
        print(e)
        return JsonResponse({'code': 10102, 'error': 'Your username is already existed~~'})

    token = make_token(username)

    try:
        code = "%s" % (random.randint(1000, 9999))
        code_str = code + '_' + username
        active_code = base64.urlsafe_b64encode(code_str.encode())
        cache.set('email_active_%s' % (username), code, 60 * 60 * 24 * 3)
        verify_url = 'http://127.0.0.1:7000/dadashop/templates/active.html?code=%s' % (active_code.decode())
        print(verify_url)
        send_active_email_async.delay(email, verify_url)

    except Exception as e:
        print('---active error---')
        print(e)

    return JsonResponse({'code': 200, 'username': username, 'data': {'token': token.decode()}, 'carts_count': 0})


def active_view(request):
    if request.method != 'GET':
        return JsonResponse({'code': 10103, 'error': 'Please use GET'})

    code = request.GET.get('code')
    if not code:
        return JsonResponse({'code': 10104, 'error': 'no code'})

    verify_code = base64.urlsafe_b64decode(code.encode()).decode()
    random_code, username = verify_code.split('_')
    old_code = cache.get('email_active_%s' % username)
    if not old_code:
        return JsonResponse({'code': 10105, 'error': 'The link is invalid'})
    if old_code != random_code:
        return JsonResponse({'code': 10106, 'error': 'The link is invalid!!'})

    user = UserProfile.objects.get(username=username)
    user.is_active = True
    user.save()

    cache.delete('email_active_%s' % (username))

    return JsonResponse({'code': 200, 'data': 'ok'})


class AddressView(View):
    @login_check
    def dispatch(self, request, *args, **kwargs):
        json_str = request.body
        if json_str:
            json_obj = json.loads(json_str)
            request.json_obj = json_obj
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, username):
        user = request.myuser

        all_address = user.address_set.filter(is_active=True)
        res = []
        for add in all_address:
            add_dict = {
                'id': add.id,
                'address': add.address,
                'receiver': add.receiver,
                'receiver_mobile': add.receiver_mobile,
                'tag': add.tag,
                'postcode': add.postcode,
                'is_default': add.is_default
            }
            res.append(add_dict)
        return JsonResponse({'code': 200, 'addresslist': res})

    def post(self, request, username):
        data = request.json_obj
        tag = data['tag']
        receiver = data['receiver']
        receiver_phone = data['receiver_phone']
        address = data['address']
        postcode = data['postcode']

        user = request.myuser

        is_default = False
        old_address = Address.objects.filter(user_profile=user)

        if not old_address:
            is_default = True

        Address.objects.create(
            user_profile=user,
            receiver=receiver,
            address=address,
            is_default=is_default,
            receiver_mobile=receiver_phone,
            postcode=postcode,
            tag=tag,
        )
        return JsonResponse({'code': 200, 'data': '新增地址成功'})

    def put(self, request):
        pass

    def delete(self, request):
        pass


def oauth_url_view(request):
    params = {
        'client_id': settings.WEIBO_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': settings.WEIBO_REDIRECT_URI
    }
    weibo_url = 'https://api.weibo.com/oauth2/authorize?'
    oauth_url = weibo_url + urlencode(params)
    return JsonResponse({'code': 200, 'oauth_url': oauth_url})


class OauthWeiboView(View):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return JsonResponse({'code': 10109, 'error': 'no code'})

        params = {
            'client_id': settings.WEIBO_CLIENT_ID,
            'client_secret': settings.WEIBO_CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.WEIBO_REDIRECT_URI
        }

        token_url = 'https://api.weibo.com/oauth2/access_token'

        # 向服务器发送POST，获得access_token
        response = requests.post(token_url, data=params)

        if response.status_code == 200:
            weibo_data = json.loads(response.text)
        else:
            print('weibo server error: %s' % response.status_code)
            return JsonResponse({'code': 10110, 'error': 'Oauth server error.'})

        if weibo_data.get('error'):
            print(weibo_data.get('error'))
            return JsonResponse({'code': 10111, 'error': 'Oauth server error.'})

        # {'access_token': '2.00lMuI2G5Cw87C59f6f57154CY_aOC', 'remind_in': '157679999', 'expires_in': 157679999, 'uid': '5809222727', 'isRealName': 'true'}
        print(weibo_data)

        weibo_uid = weibo_data['uid']
        access_token = weibo_data['access_token']
        try:
            weibo_user = WeiboProfile.objects.get(wuid=weibo_uid)
        except Exception as e:
            print(e)
            WeiboProfile.objects.create(access_token=access_token, wuid=weibo_uid)
            return JsonResponse({'code': 201, 'uid': weibo_uid})
        else:
            # 之前来过，是否绑定
            user = weibo_user.user_profile
            if user:
                # 成功注册并绑定
                username = user.username
                token = make_token(username)
                return JsonResponse({'code': 200, 'username': username, 'token': token.decode()})
            else:
                # 未绑定
                return JsonResponse({'code': 201, 'uid': weibo_uid})

    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        uid = data['uid']
        email = data['email']
        phone = data['phone']

        m = hashlib.md5()
        m.update(password.encode())
        password_h = m.hexdigest()

        try:
            with transaction.atomic():
                user = UserProfile.objects.create(username=username, password=password_h, email=email, phone=phone)
                weibo_user = WeiboProfile.objects.get(wuid=uid)
                weibo_user.user_profile = user
                weibo_user.save()
        except Exception as e:
            print(e)
            return JsonResponse({'code': 10112, 'error': 'create user error.'})

        token = make_token(username)

        try:
            randnum = "%s" % (random.randint(1000, 9999))
            code_str = randnum + '_' + username
            active_code = base64.urlsafe_b64encode(code_str.encode())
            cache.set('email_active_%s' % username, randnum, 60 * 60 * 24 * 3)
            verify_url = 'http://127.0.0.1:7000/dadashop/templates/active.html?code=%s' % (active_code.decode())
            send_active_email_async.delay(email, verify_url)
        except Exception as e:
            print('---active error---')
            print(e)

        return JsonResponse({'code': 200,
                             'username': username,
                             'token': token.decode()})
