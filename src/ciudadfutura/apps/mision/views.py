from django.shortcuts import render


def index(request):

    return render(request, 'mision/index.html', {
        'page_title': 'Mision',
    })


def register(request):

    return render(request, 'mision/register.html', {
        'page_title': 'Mision Register',
    })
