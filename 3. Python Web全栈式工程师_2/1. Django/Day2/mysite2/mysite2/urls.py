from django.urls import path, re_path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_get', views.test_get),
    path('test_post', views.test_post),
    re_path(r'^test$', views.test),
    re_path(r'^mycal$', views.calculate)
]
