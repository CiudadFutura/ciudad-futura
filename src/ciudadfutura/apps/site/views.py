from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from ciudadfutura.decorators import user_required
from ciudadfutura.apps.mision.forms import LoginForm
from django.core.urlresolvers import reverse_lazy as reverse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm, UserPublicProfileForm, MyCircleForm
from ciudadfutura.apps.auth.models import MisionMember
from ciudadfutura.utils import paginate

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


@user_required
def user_dashboard(request):
    return render(request, 'site/user_dashboard.html', {
        'user': request.user,
    })


@user_required
def user_public_profile(request):

    user = request.user

    if request.POST:
        form = UserPublicProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('site:ciudadfutura-user-dashboard')
    else:
        form = UserPublicProfileForm(instance=user)

    return render(request, 'site/user_public_profile_tab.html', {
        'form': form,
        'active': 'user_public_profile'
    })


@user_required
def user_private_profile(request):

    user = request.user

    if request.POST:
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('site:ciudadfutura-user-private-profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'site/user_private_profile_tab.html', {
        'form': form,
        'active': 'user_private_profile'
    })


@user_required
def user_change_password(request):
    user = request.user
    data = {}

    if request.POST:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('site:ciudadfutura-user-change-password')
    else:
        form = PasswordChangeForm(user=user)

    return render(request, 'site/reset_password_form.html', {
        'form': form,
        'active': 'user_change_password'
    })


@user_required
def user_reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request,
                                  template_name='site/user_reset_confirm.html',
                                  uidb36=uidb36,
                                  token=token,
                                  post_reset_redirect=reverse('site:login'))


@user_required
def user_reset(request):

    return password_reset(request,
                          template_name='site/reset_password_form.html',
                          email_template_name='site/reset_password_email.html',
                          subject_template_name='site/reset_password_subject.txt',
                          post_reset_redirect=reverse('site:login'))


@user_required
def user_circle(request):
    circle_members = request.user.member.circle.member.all()

    return render(request, 'site/user_circle_list.html', {
        'results':  circle_members,
        'active': 'user_my_circle'
    })
