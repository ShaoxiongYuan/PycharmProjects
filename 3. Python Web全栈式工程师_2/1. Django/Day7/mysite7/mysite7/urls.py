from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cache$', views.test_cache),
    url(r'^middleware$', views.test_middleware),
    url(r'^csrf$', views.test_csrf)
]
