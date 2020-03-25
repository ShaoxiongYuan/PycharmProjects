from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_get', views.test_get),
    path('test_post', views.test_post)
]
