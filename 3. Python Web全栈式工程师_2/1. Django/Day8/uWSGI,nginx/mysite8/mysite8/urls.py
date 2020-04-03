from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test_page$', views.test_page, name='book'),
    url(r'^upload$', views.upload_view),
    url(r'^download$', views.download_view)
]
