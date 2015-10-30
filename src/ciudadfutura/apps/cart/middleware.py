from .models import Cart


class CartMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):

        user = request.user
        if user.is_authenticated() and user.has_relation.MISION:
            request.cart = user.member.cart or Cart()

            if not request.cart.pk:
                request.cart.save()
                user.member.cart = request.cart
                user.member.save(update_fields=['cart'])

        else:
            request.cart = None
