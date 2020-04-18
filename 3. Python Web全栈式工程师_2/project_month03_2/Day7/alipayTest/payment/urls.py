from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^jump$', views.OrderInfoView.as_view()),
    url(r'^result$', views.ResultView.as_view())
]
