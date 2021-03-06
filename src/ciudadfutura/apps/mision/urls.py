from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mision/$', views.index, name='index'),
    url(r'^mision/register/$', views.register, name='register'),
    url(r'^mision/product/$', views.product_list, name='product-list'),
    url(r'^mision/confirm/(?P<code>\w+)/', views.account_confirm, name='invite-confirm'),
]
