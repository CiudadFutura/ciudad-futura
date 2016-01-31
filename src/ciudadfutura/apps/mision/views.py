# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from ciudadfutura.utils import paginate
from django.views.generic import TemplateView
from ciudadfutura.apps.product.models import Product, Category
from ciudadfutura.apps.mision.models import Invite
from ciudadfutura.decorators import user_required
from .forms import UserForm, InviteForm, InviteRegisterForm
from django.core.mail import EmailMessage
from hashlib import sha1
from uuid import uuid4
from django.shortcuts import get_object_or_404
from django.conf import settings


def index(request):
    return render(request, 'mision/index.html', {
        'page_title': 'Mision'
    })


def register(request):

    if request.user.is_authenticated():
        return redirect('mision:product-list')

    invite_forms = []

    if request.POST:

        for idx, email in enumerate(request.POST.getlist('invite-email')):
            invite_forms.append(
                InviteForm({
                    'invite-email': email,
                    'invite-first_name': request.POST.getlist('invite-first_name')[idx],
                    'invite-last_name': request.POST.getlist('invite-last_name')[idx],
                }, prefix='invite')
            )

        form = UserForm(request.POST)

        if all([form.is_valid()] + [f.is_valid() for f in invite_forms]):
            member = form.save()
            for f in invite_forms:
                invite = f.save(commit=False)
                invite.circle = member.circle
                invite.code = uuid4().hex
                invite.activation_key = sha1(invite.email + invite.code).hexdigest()
                invite.save()
                send_email(request, member, invite)

            messages.success(request, _('User successfully saved.'))
            return redirect('account:ciudadfutura-user-dashboard')
    else:
        invite_forms = [
            InviteForm(prefix='invite'), InviteForm(prefix='invite')
        ]
        form = UserForm(initial={
            'invites': len(invite_forms)
        })

    return render(request, 'mision/register.html', {
        'form': form,
        'invite': {
            'tpl': InviteForm(prefix='invite'),
            'forms': invite_forms,
        },
    })


def product_list(request):

    selected = [
        int(category_id) for category_id in request.GET.getlist('categories')
    ]

    results = Product.objects.all()
    if selected:
        results = results.filter(parent__in=selected)

    return render(request, 'mision/product_list.html', {
        'results': paginate(request.GET, results),
        'categories': Category.objects.filter(parent__isnull=True),
        'selected': selected
    })


def account_confirm(request, code=None):

    invite = None

    if code is not None:
        invite = get_object_or_404(Invite, code=code)

    if request.POST:
        form = InviteRegisterForm(request.POST, instance=invite)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('Invite successfully saved.'))
            return redirect('account:ciudadfutura-user-dashboard')
    else:
        invite = Invite.objects.get(code=code)
        if invite:
            if sha1(invite.email + invite.code).hexdigest() == invite.activation_key:
                data = {
                    'code': invite.code,
                    'circle': invite.circle_id
                }
                form = InviteRegisterForm(instance=invite, initial=data)
            else:
                messages.success(request, _('The code does not exist.'))
                render(request, 'mision:index')

    return render(request, 'mision/invite_register.html', {
        'form': form,
    })


def send_email(request, member, invite):
    # Send email with activation key
    current_site = getattr(settings, 'SITE_HOST_NAME', 'defaulthostname')
    message = "Hola %s, El coordinador %s te invito a ser parte de la Mision y de su circulo. Para aceptar la " \
            "invitacion tienes que hacer clic en: %s/%s" \
            % (invite.first_name, member.user.name, current_site, invite.code)
    msg = EmailMessage(subject="Bienvenido - Acepta la Invitacion",
                       body=message,
                       from_email='victoriacolectiva@gmail.com',
                       to=[invite.email])

    msg.send()
