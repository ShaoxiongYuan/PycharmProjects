from django.urls import re_path
from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^cache$', views.test_cache),
    re_path(r'^middleware$', views.test_middleware),
    re_path(r'^csrf$', views.test_csrf)
]
