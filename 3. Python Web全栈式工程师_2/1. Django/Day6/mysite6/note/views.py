from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session:
            if 'username' not in request.COOKIES:
                return HttpResponseRedirect('/user/login')
            else:
                username = request.COOKIES['username']
                request.session['username'] = username
        return fn(request, *args, **kwargs)

    return wrap


@check_login
def add_view(request):
    if request.method == 'GET':
        return HttpResponse('--可添加')
    return HttpResponse('--Your method is wrong ~')
