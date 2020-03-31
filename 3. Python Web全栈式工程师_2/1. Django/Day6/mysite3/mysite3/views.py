from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def test(request):
    dict1 = {
        "username": "steven",
        "age": 18,
        "note": "我叫笑笑笑哈哈哈哈"
    }
    return render(request, 'test.html', dict1)


def index(request):
    dict1 = {
        "lst": ["Tom", "Jack"]
    }
    return render(request, 'base.html', dict1)


def test_music(request):
    return render(request, 'music.html')


def test_sport(request):
    return render(request, 'sport.html')


def page1_view(request):
    return render(request, 'page1.html')


def page2_view(request):
    return HttpResponse('我是page2')


def pagen_view(request, n):
    print(reverse('page2'))
    # print(reverse('pn', args=['500']))
    print(reverse('pn', kwargs={'n': 500}))
    return HttpResponse('我是page%s' % n)


def test_static(request):
    return render(request, 'static.html')


def test_cookies(request):
    username = request.COOKIES.get('username', '哈哈哈')
    print(username)
    response = HttpResponse('哈哈哈')
    response.set_cookie('username', 'steven', 300)
    # response.set_cookie('user', 'steven')
    return response


def set_session(request):
    request.session['uname'] = 'steven'
    return HttpResponse('set session is OK.')


def get_session(request):
    name = request.session.get('uname')
    return HttpResponse('get session: %s' % name)
