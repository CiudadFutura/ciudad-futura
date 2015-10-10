from .models import Cart


class CartMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):

        user = request.user
        if user.is_authenticated() and user.has_relation.MISION:
            request.cart = user.member.cart or Cart.objects.create()
