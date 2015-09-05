from django.shortcuts import render


def index(request):

    form = None

    return render(request, 'site/index.html', {
    })
