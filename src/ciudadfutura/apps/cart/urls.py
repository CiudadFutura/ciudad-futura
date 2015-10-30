from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cart/$',
        views.index,
        name='index'),
    url(r'^cart/add-item/(?P<product_id>\d+)/$',
        views.add_item,
        name='add-item'),
    url(r'^cart/remove-item/(?P<item_id>\d+)/$',
        views.remove_item,
        name='remove-item'),
]
