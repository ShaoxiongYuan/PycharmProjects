from django.http import HttpResponse


# Create your views here.
def index_view(request):
    return HttpResponse('This is sports index.')
