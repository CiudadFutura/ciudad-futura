from django.conf.urls import url
from . import views


def cart_urls(prefix, template):
    return [
        url(r'^{prefix}/cart/$'.format(prefix=prefix),
            views.index(template),
            name='cart'),
        url(r'^{prefix}/cart/add-item/(?P<product_id>\d+)/$'.format(prefix=prefix),
            views.add_item,
            name='cart-add-item'),
        url(r'^{prefix}/cart/remove-item/(?P<item_id>\d+)/$'.format(prefix=prefix),
            views.remove_item,
            name='cart-remove-item'),
    ]
