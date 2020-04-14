from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.users),
    url(r'^/activation$', views.active_view),
    url(r'^/(?P<username>\w+)/address$', views.AddressView.as_view()),
    url(r'^/weibo/authorization$', views.oauth_url_view),
    url(r'^/weibo/users$',views.OauthWeiboView.as_view())
]
