from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/(?P<username>\w+)$', views.CartsView.as_view())
]
