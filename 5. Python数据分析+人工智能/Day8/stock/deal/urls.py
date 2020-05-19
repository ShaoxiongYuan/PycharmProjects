from django.conf.urls import url
from deal import views

urlpatterns = [
    url(r'tobuy', views.Tobuy, name= "tobuy"),
    url(r'tosell', views.Tosale, name="tosale"),
    url(r'trade', views.trade, name='trade'),
    url(r'bosstock', views.allstock, name='bosstock'),


]
