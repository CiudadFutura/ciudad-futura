from .models import Cart
from django.contrib import messages


class CartMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):

        user = request.user

        if 'cart_id' not in request.session:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
            request.session.save()
        else:
            cart_id = request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)

        request.cart = cart

        if user.is_authenticated() and hasattr(user, 'member'):
            user.member.cart = cart
            user.member.save(update_fields=['cart'])
