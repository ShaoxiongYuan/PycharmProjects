from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/(?P<username>\w+)/advance$', views.AdvanceOrderView.as_view())
]
