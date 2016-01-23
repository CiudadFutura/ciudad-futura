from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CheckoutForm
from pprint import pprint
import logging
from ciudadfutura.apps.cart.models import Cart
from ciudadfutura.apps.order.models import Order


def index(template):

    def actual_view(request):
        items = []
        if request.cart:
            items = request.cart.items.all()

        return render(request, template, {
            'cart': request.cart,
            'items': items
        })

    actual_view.__name__ = 'order_index'

    return actual_view


def checkout(request):

    order = None
    if request.POST and request.POST['cartId']:
        if request.user.is_authenticated():
            order = Order.objects.create(user_id=request.user.id)
            order.add_item(cart_id=request.POST['cartId'])

            messages.success(request, _('Order successfully created.'))

            return redirect('mision:success-checkout', order.id)
        else:
            messages.error(request, 'You should be logged to confirm the order.')
            return redirect('site:login')
    else:
        return render(request, 'mision:cart')


def success(request, code=None):
    order = Order.objects.get(id=code)
    return render(request, 'mision/success.html', {
        'order': order,
    })


