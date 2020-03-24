from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.main_view),
    path('page1', views.page1_view),
    path('page2', views.page2_view),
    re_path(r'page(\d+)', views.pagen_view),
    re_path(r'^(\d+)/(\S+)/(\d+)', views.calculate_view),
    re_path(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})', views.person_view),
    re_path(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})', views.birth_view),
    re_path(r'^birthday/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})', views.birth_view),
]
