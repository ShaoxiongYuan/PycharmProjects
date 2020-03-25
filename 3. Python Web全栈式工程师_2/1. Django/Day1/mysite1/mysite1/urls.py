from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.main_view),
    url('page1', views.page1_view),
    url('page2', views.page2_view),
    url(r'^page(\d+)', views.pagen_view),
    url(r'^(\d+)/(\S+)/(\d+)', views.calculate_view),
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})', views.person_view),
    url(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})', views.birth_view),
    url(r'^birthday/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})', views.birth_view),
]
