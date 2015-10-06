from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from ciudadfutura.decorators import staff_required
from ciudadfutura.apps.auth.models import User, Tag, MisionMember
from ciudadfutura.apps.mision.models import Invite
from ciudadfutura.utils import paginate
from .forms import LoginForm, UserForm, TagForm, InviteForm
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, RedirectView, TemplateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions


class IndexView(TemplateView):
    template_name = "mision/index.html"

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data()
        ctx['page_title'] = 'Mision'
        return ctx


class RegisterView(CreateView):
    template_name = "mision/register.html"
    model = MisionMember
    form_class = UserForm
    success_url = 'success'

    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form, member=self.request.member)

    def get_context_data(self, **kwargs):
        ctx = super(RegisterView, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Mision'
        return ctx


def register(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('site:ciudadfutura-user-dashboard')
    else:
        form = UserForm()

    return render(request, 'mision/register.html', {
        'form': form,
        'invite_form': InviteForm()
    })


index = IndexView.as_view()
