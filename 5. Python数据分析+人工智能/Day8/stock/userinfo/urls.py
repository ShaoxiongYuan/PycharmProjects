from django.conf.urls import url
from django.contrib import admin
from userinfo import views

urlpatterns = [
    url(r'login', views.login_, name='login'),
    url(r'register', views.register_, name='register'),
    url(r'logout', views.logout_, name='logout'),
    url(r'info', views.info, name='info'),
    url(r'charge', views.charge),
    url(r'changepwd', views.change_pwd),
    url(r'bankbg', views.bankbg),



]