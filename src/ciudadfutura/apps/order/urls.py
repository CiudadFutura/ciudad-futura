from django.conf.urls import url
from . import views


def order_urls(prefix, template):
    return [
        url(r'^{prefix}/checkout/$'.format(prefix=prefix),
            views.index(template),
            name='checkout'),
    ]
