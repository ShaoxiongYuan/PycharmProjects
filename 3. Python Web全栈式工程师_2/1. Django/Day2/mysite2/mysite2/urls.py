from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('test_get', views.test_get),
    url('test_post', views.test_post),
    url(r'^test$', views.test),
    url(r'^mycal$', views.calculate)
]
