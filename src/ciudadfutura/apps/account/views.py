from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from ciudadfutura.decorators import user_required
from django.core.urlresolvers import reverse_lazy as reverse
from django.contrib import messages
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm, UserPublicProfileForm
from ciudadfutura.apps.order.models import Order, OrderItem


@user_required
def index(request):
    return redirect('account:ciudadfutura-user-public-profile')


@user_required
def user_public_profile(request):

    user = request.user

    if request.POST:
        form = UserPublicProfileForm(
            request.POST, request.FILES, instance=user
        )
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('account:ciudadfutura-user-public-profile')
    else:
        form = UserPublicProfileForm(instance=user)

    return render(request, 'account/user_public_profile_tab.html', {
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
            return redirect('account:ciudadfutura-user-private-profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'account/user_private_profile_tab.html', {
        'form': form,
        'active': 'user_private_profile'
    })


@user_required
def user_change_password(request):
    user = request.user

    if request.POST:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('account:ciudadfutura-user-change-password')
    else:
        form = PasswordChangeForm(user=user)

    return render(request, 'account/reset_password_form.html', {
        'form': form,
        'active': 'user_change_password'
    })


@user_required
def user_reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request, {
        'template_name': 'account/user_reset_confirm.html',
        'uidb36': uidb36,
        'token': token,
        'post_reset_redirect': reverse('site:login')
    })


@user_required
def user_reset(request):
    return password_reset(request, {
        'template_name': 'account/reset_password_form.html',
        'email_template_name': 'account/reset_password_email.html',
        'subject_template_name': 'account/reset_password_subject.txt',
        'post_reset_redirect': reverse('site:login')
    })


@user_required
def user_circle(request):
    circle_members = request.user.member.circle.member.all()

    return render(request, 'account/user_circle_list.html', {
        'results':  circle_members,
        'active': 'user_my_circle'
    })


@user_required
def user_orders(request):
    orders = request.user.orders.all()

    return render(request, 'account/user_orders_list.html', {
        'results':  orders,
        'active': 'user_my_orders'
    })


def user_order_details(request, order_id):
    items = OrderItem.objects.filter(order_id=order_id)
    return render(request, 'account/user_order_details.html', {
        'items': items,
        'active': 'user_my_orders'
    })
