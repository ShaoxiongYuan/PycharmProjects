from django.urls import re_path
from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^test_page$', views.test_page, name='book'),
    re_path(r'^upload$', views.upload_view),
    re_path(r'^download$', views.download_view)
]
