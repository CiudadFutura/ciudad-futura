from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^mision/$', views.index, name='mision'),
    url(r'^mision/register/$', views.register, name='mision-register'),
]
