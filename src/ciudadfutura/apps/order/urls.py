from django.conf.urls import url
from . import views


def order_urls(prefix, template):
    return [
        url(r'^{prefix}/checkout/$'.format(prefix=prefix),
            views.index(template),
            name='checkout'),
        url(r'^{prefix}/confirm_checkout/$'.format(prefix=prefix),
            views.checkout,
            name='confirm-checkout'),
        url(r'^{prefix}/success'.format(prefix=prefix),
            views.success,
            name='success-checkout'),

    ]
