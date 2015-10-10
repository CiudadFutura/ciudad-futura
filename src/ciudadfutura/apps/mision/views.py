from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, InviteForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "mision/index.html"

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data()
        ctx['page_title'] = 'Mision'
        return ctx


def register(request):

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
                invite.save()

            messages.success(request, _('User successfully saved.'))
            return redirect('site:ciudadfutura-user-dashboard')
    else:
        invite_forms = [InviteForm(prefix='invite'), InviteForm(prefix='invite')]
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


index = IndexView.as_view()
