from django.http import HttpResponse, HttpResponseRedirect


def main_view(request):
    return HttpResponse('<h1>这是我的首页</h1>')


def page1_view(request):
    html = "<h1>这是编号为1的页面</h1>"
    # return JsonResponse(html, safe=False)
    # return HttpResponse(html)
    # 302跳转依靠Response Header里的Location
    return HttpResponseRedirect('/page2')


def page2_view(request):
    html = "<h1>这是编号为2的页面</h1>"
    return HttpResponse(html)


def pagen_view(request, num):
    html = "<h1>——————这是编号为" + num + "的页面——————</h1>"
    return HttpResponse(html)


def calculate_view(request, num1, op, num2):
    num1 = int(num1)
    num2 = int(num2)
    if op == 'add':
        res = num1 + num2
    elif op == 'sub':
        res = num1 - num2
    elif op == 'mul':
        res = num1 * num2
    else:
        return HttpResponse("I am sorry.")
    return HttpResponse(res)


def person_view(request, name, age):
    return HttpResponse("姓名:%s，年龄:%s" % (name, age))


def birth_view(request, year, month, day):
    print(request.path_info)
    print(request.get_full_path())
    print(request.META)
    print(request.META['REMOTE_ADDR'])
    print(request.method)
    # print(request.encoding)
    # print(request.scheme)
    # print(request.COOKIES)
    # print(request.body.decode())
    # print(request.session)
    # print(request.environ)
    # print(request.GET)
    # print(request.POST)
    return HttpResponse("生日为：%s年%s月%s日" % (year, month, day))
