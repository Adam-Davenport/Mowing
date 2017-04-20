from django.conf.urls import url
from record import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^farm/$', views.farm, name='farm'),
    url(r'^trails/$', views.trails, name='trails'),
]