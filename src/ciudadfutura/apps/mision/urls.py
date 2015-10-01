from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^mision/$', views.index, name='index'),

    url(r'^mision/register/$', views.register, name='register'),

]
