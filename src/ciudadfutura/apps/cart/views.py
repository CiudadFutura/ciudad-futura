from django.utils.translation import ugettext as _
from django.http.response import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    results = []
    if request.cart:
        results = request.cart.items.all()

    return render(request, 'mision/cart.html', {
        'results': results
    })


def add_item(request, product_id):

    if request.POST and request.cart:
        item = request.cart.add_item(
            product_id, request.POST['quantity']
        )
        return JsonResponse({
            'success': True,
            'total_items': request.cart.total_items,
            'item': {
                'name': item.name,
            }
        })

    return HttpResponseBadRequest()


def remove_item(request, item_id):

    if request.cart:
        request.cart.remove_item(item_id)
        messages.success(request, _('Item successfully removed.'))

    return redirect('cart:index')
