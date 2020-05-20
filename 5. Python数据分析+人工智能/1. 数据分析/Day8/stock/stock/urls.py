"""stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('userinfo.urls')),
    url(r'^stock/', include('stocks.urls')),
    url(r'^deal/', include('deal.urls')),
    #url(r'^pay/', include('pay.urls')),
    url(r'^index-1', TemplateView.as_view(template_name="index-1.html"), name='index'),
    url(r'^header', TemplateView.as_view(template_name="header.html"), name='header'),
    url(r'^index-2', TemplateView.as_view(template_name="index-2.html"), name='index'),
    url(r'^index-3', TemplateView.as_view(template_name="index-3.html"), name='index'),
    url(r'^index-4', TemplateView.as_view(template_name="index-4.html"), name='index'),
]
