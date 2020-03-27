from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test$', views.test),
    url(r'^base$', views.index, name='base'),
    url(r'^music$', views.test_music),
    url(r'^sport$', views.test_sport),
    url(r'^page1$', views.page1_view, name='page1'),
    url(r'^page2$', views.page2_view, name='page2'),
    # url(r'^page(\d+)', views.pagen_view, name='pn'),
    url(r'^page(?P<n>\d+)', views.pagen_view, name='pn'),
]
