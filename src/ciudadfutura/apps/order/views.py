from django.shortcuts import render


def index(template):

    def actual_view(request):
        items = []
        if request.cart:
            items = request.cart.items.all()

        return render(request, template, {
            'items': items
        })

    actual_view.__name__ = 'order_index'

    return actual_view
