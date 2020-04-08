from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(\d+)$', views.user_detail),
    url(r'^update$', views.update_detail)
]
