from django.http import HttpResponse
import redis
from .models import User

r = redis.Redis(host='127.0.0.1', db=0, port=6379)


# Create your views here.
def user_detail(request, user_id):
    cache_key = 'user:%s' % user_id
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        new_data = {k.decode(): v.decode() for k, v in data.items()}
        nickname = new_data['nickname']
        age = new_data['age']
        html = 'nickname is %s, age is %s' % (nickname, age)
        return HttpResponse(html)
    else:
        users = User.objects.filter(id=user_id)
        user = users[0]
        nickname = user.nickname
        age = user.age
        html = 'mysql nickname is %s, age is %s' % (nickname, age)
        r.hmset(cache_key, {'nickname': nickname, 'age': age})
        r.expire(cache_key, 15)
        return HttpResponse(html)


def update_detail(request):
    user_id = request.GET.get('user_id')
    nickname = request.GET.get('nickname')
    age = request.GET.get('age')

    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        print(e)
        return HttpResponse('--no match--')

    if nickname:
        user.nickname = nickname
    if age:
        user.age = age
    user.save()

    r.delete('user:' + user_id)
    return HttpResponse('更新成功')
