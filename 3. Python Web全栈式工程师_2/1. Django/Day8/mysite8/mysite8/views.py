from django.core.paginator import Paginator
from django.shortcuts import render


def test_page(request):
    all_data = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(all_data, 2)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'test_page.html', locals())


def upload(request):
    request
