from django.urls import re_path, include
from django.contrib import admin

from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^test$', views.test),
    re_path(r'^base$', views.index, name='base'),
    re_path(r'^music$', views.test_music),
    re_path(r'^sport$', views.test_sport),
    re_path(r'^page1$', views.page1_view, name='page1'),
    re_path(r'^page2$', views.page2_view, name='page2'),
    # re_path(r'^page(\d+)', views.pagen_view, name='pn'),
    re_path(r'^page(?P<n>\d+)', views.pagen_view, name='pn'),
    re_path(r'^static$', views.test_static),
    re_path(r'^music/', include('music.urls')),
    re_path(r'^sport/', include('sport.urls')),
    re_path(r'^news/', include('news.urls')),
    re_path(r'^bookstore/', include('bookstore.urls')),
    re_path(r'^cookie$', views.test_cookies),
    re_path(r'^set_session$', views.set_session),
    re_path(r'^get_session$', views.get_session)
]
