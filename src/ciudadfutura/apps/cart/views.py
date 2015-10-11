from django.http.response import JsonResponse, HttpResponseBadRequest


def add_item(request, product_id):

    if request.POST and request.cart:
        item = request.cart.add_item(
            product_id, request.POST['quantity']
        )
        return JsonResponse({
            'success': True,
            'item': {
                'name': item.name,
            }
        })

    return HttpResponseBadRequest()


def remove_item(request, product_id):

    if request.POST and request.cart:
        request.cart.remove_item(product_id)
        return JsonResponse({
            'success': True,
        })

    return HttpResponseBadRequest()
