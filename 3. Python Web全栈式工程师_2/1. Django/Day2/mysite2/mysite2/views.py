from django.http import HttpResponse
from django.shortcuts import render


def say_hi():
    return "Hello Everyone"


class Dog:
    def say(self):
        return "hahahahaha"


dog = Dog()


def test_get(request):
    if request.method == 'GET':
        print(request.GET)
        print(request.GET.getlist('a'))
        print(request.GET.get('b', 'hahaha'))
        return HttpResponse('test get is OK.')
    return HttpResponse('test get is error')


def test_post(request):
    if request.method == 'GET':
        html = """
        <form method='POST' action="/test_post">
            姓名:<input type="text" name="uname">
            密码:<input type="password" name="pwd">
            <input type='submit' value='登录'>
        </form>
        """
        return HttpResponse(html)
    elif request.method == 'POST':
        username = request.POST.get('uname', 'hahaha')
        print(username)
        return HttpResponse('test post is OK.')


def test(request):
    # t = loader.get_template('test.html')
    # html = t.render()
    # return HttpResponse(html)
    dict1 = {
        "username": "steven",
        "age": 18,
        "lst": [1, 2],
        "d": {"name": "steven"},
        "func": say_hi,
        "class_obj": dog.say(),
        "script": "<script>alert('good')</script>"
    }
    return render(request, 'test.html', dict1)


def calculate(request):
    if request.method == 'GET':
        return render(request, 'calculate.html')
    elif request.method == 'POST':
        op = request.POST.get('op')
        try:
            x = int(request.POST.get('x'))
            y = int(request.POST.get('y'))
        except:
            x = request.POST.get('x')
            y = request.POST.get('y')
            res = 'No result'
        else:
            if op == 'add':
                res = x + y
            elif op == 'sub':
                res = x - y
            elif op == 'mul':
                res = x * y
            elif op == 'div':
                res = x / y
        finally:
            return render(request, 'calculate.html', locals())
