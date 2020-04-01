from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


# Create your views here.
def check_login(fn):
    def wrapper(request, *args, **kwargs):
        if 'username' not in request.session:
            if 'username' not in request.COOKIES:
                return HttpResponseRedirect('/user/login')
            else:
                username = request.COOKIES['username']
                request.session['username'] = username
        return fn(request, *args, **kwargs)

    return wrapper


@check_login
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    return HttpResponse('--Your method is wrong ~')
