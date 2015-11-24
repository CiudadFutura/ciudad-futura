from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from ciudadfutura.decorators import user_required
from ciudadfutura.apps.mision.forms import LoginForm
from django.core.urlresolvers import reverse_lazy as reverse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

from .forms import UserProfileForm


def index(request):
    return render(request, 'site/index.html', {
        'body_class': 'site-view-home',
    })


def user_logout(request):
    auth.logout(request)
    messages.success(request, _('You have successfully logged out.'))
    return redirect('site:ciudadfutura-home')


def user_login(request):
    form = None

    if request.user.is_authenticated():
        return redirect('site:ciudadfutura-user-dashboard')

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None and user.is_active:
                auth.login(request, user)
                messages.success(request, _('Authentication succeed.'))
                return redirect('site:ciudadfutura-user-dashboard')

        messages.error(request, _('Authentication failed.'))
    else:
        form = LoginForm()

    return render(request, 'site/user_login.html', {
        'form': form
    })


@user_required(login_url=reverse('site:ciudadfutura-user-login'))
def user_dashboard(request):
    return render(request, 'site/user_dashboard.html', {
        'user': request.user,
    })


@user_required(login_url=reverse('site:ciudadfutura-user-login'))
def user_profile(request):

    user = request.user

    if request.POST:

        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('site:ciudadfutura-user-dashboard')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'site/user_profile_tab.html', {
        'form': form,
        'active': 'user_profile'
    })


@user_required(login_url=reverse('site:ciudadfutura-user-login'))
def user_change_password(request):
    user = request.user
    data = {}

    if request.POST:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('site:ciudadfutura-user-profile')
    else:
        form = PasswordChangeForm(user=user)

    return render(request, 'site/reset_password_form.html', {
        'form': form,
        'active': 'user_change_password'
    })


@user_required(login_url=reverse('site:ciudadfutura-user-login'))
def user_reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request,
                                  template_name='site/user_reset_confirm.html',
                                  uidb36=uidb36,
                                  token=token,
                                  post_reset_redirect=reverse('site:ciudadfutura-user-login'))


@user_required(login_url=reverse('site:ciudadfutura-user-login'))
def user_reset(request):

    return password_reset(request,
                          template_name='site/reset_password_form.html',
                          email_template_name='site/reset_password_email.html',
                          subject_template_name='site/reset_password_subject.txt',
                          post_reset_redirect=reverse('site:ciudadfutura-user-login'))
