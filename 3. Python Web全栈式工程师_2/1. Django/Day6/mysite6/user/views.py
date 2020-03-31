from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import hashlib


# Create your views here.
def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/reg.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        # TODO 参数检查
        if password_1 != password_2:
            error = 'The password is not the same~'
            return render(request, 'user/reg.html', locals())

        old_users = User.objects.filter(username=username)
        if old_users:
            error = 'The username already exists.'
            return render(request, 'user/reg.html', locals())

        m = hashlib.md5()  # 获取计算对象
        m.update(password_1.encode())  # 更新明文
        password_h = m.hexdigest()  # 获取16进制结果

        try:
            user = User.objects.create(username=username, password=password_h)
        except Exception as e:
            print(e)
            error = 'The username already exists.'
            return render(request, 'user/reg.html', locals())

        request.session['username'] = username
        return HttpResponse('---reg ok---')

    return HttpResponse('--Your method is wrong')


def login_view(request):
    if request.method == 'GET':
        if 'username' in request.session:
            return HttpResponse('---已登录')
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
            request.session['username'] = username
            return HttpResponse('--已登录')

        return render(request, 'user/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username=username)
        if not users:
            error = 'The username or password is wrong'
            return render(request, 'user/login.html', locals())
        user = users[0]

        m = hashlib.md5()
        m.update(password.encode())
        c_password = m.hexdigest()

        if c_password != user.password:
            error = 'The username or password is wrong'
            return render(request, 'user/login.html', locals())

        resp = HttpResponse('--login is ok--')
        request.session['username'] = username
        if 'long' in request.POST:
            resp.set_cookie('username', username, 60 * 60 * 24 * 20)
        return resp

    return HttpResponse('Your method is worng~')
