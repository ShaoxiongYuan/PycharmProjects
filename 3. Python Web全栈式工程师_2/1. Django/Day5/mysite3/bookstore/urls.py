from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^book$', views.book, name='all_book'),
    url(r'update_book/(?P<id>\d+)', views.update),
    url(r'delete_book/(?P<id>\d+)', views.delete),
    url(r'add_book', views.add),
]
