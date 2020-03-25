from django.http import HttpResponse


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
