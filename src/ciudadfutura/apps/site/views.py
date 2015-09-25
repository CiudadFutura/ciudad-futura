from django.shortcuts import render


def index(request):
    return render(request, 'site/index.html', {})


def user_dashboard(request):
    return render(request, 'site/user_dashboard.html', {})


def user_login(request):
    return render(request, 'site/user_login.html', {})


def user_profile(request):
    return render(request, 'site/user_profile.html', {})
