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
