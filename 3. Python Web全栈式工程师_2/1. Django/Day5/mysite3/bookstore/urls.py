from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^book$', views.book, name='all_book'),
    re_path(r'update_book/(?P<id>\d+)', views.update),
    re_path(r'delete_book/(?P<id>\d+)', views.delete),
    re_path(r'add_book', views.add),
]
