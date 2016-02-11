from django.conf.urls import url
from . import views
from ciudadfutura.apps.cart.urls import cart_urls
from ciudadfutura.apps.order.urls import order_urls


urlpatterns = [
    url(r'^mision/$',
        views.index,
        name='index'),
    url(r'^mision/register/$',
        views.register,
        name='register'),
    url(r'^mision/product/$',
        views.product_list,
        name='product-list'),
    url(r'^mision/product/category/(?P<code>\w+)/',
        views.product_list,
        name='product-list-category'),
    url(r'^mision/confirm/(?P<code>\w+)/',
        views.account_confirm,
        name='invite-confirm'),
] + cart_urls(
    prefix='mision', template='mision/cart.html'
) + order_urls(
    prefix='mision', template='mision/checkout.html'
)
