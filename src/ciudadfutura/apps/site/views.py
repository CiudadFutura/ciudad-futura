from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from ciudadfutura.apps.mision.forms import LoginForm
from django.contrib import messages
from django.contrib import auth


def index(request):
    return render(request, 'site/index.html', {
        'body_class': 'site-view-home',
    })


def user_logout(request):
    auth.logout(request)
    messages.success(request, _('You have successfully logged out.'))
    return redirect('site:login')


def user_login(request):
    form = None

    if request.user.is_authenticated():
        return redirect('account:ciudadfutura-user-dashboard')

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None and user.is_active:
                auth.login(request, user)
                messages.success(request, _('Authentication succeed.'))
                return redirect('account:ciudadfutura-user-dashboard')

        messages.error(request, _('Authentication failed.'))
    else:
        form = LoginForm()

    return render(request, 'site/user_login.html', {
        'form': form
    })
