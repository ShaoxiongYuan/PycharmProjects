from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
import os
import csv


def test_page(request):
    all_data = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(all_data, 2)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'test_page.html', locals())


def upload_view(request):
    if request.method == 'GET':
        return render(request, 'upload_file.html')
    elif request.method == "POST":
        a_file = request.FILES['myfile']
        print("上传文件名是:", a_file.name)

        filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        with open(filename, 'wb') as f:
            data = a_file.file.read()
            f.write(data)
        return HttpResponse("接收文件:" + a_file.name + "成功")
    raise Http404


def download_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test.csv"'
    all_data = [{'id': 1, 'title': 'python1'}, {'id': 2, 'title': 'python2'}]
    writer = csv.writer(response)
    writer.writerow(['id', 'title'])
    for data in all_data:
        writer.writerow([data['id'], data['title']])
    return response
