from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from ciudadfutura.decorators import staff_required
from ciudadfutura.apps.auth.models import User, Tag, MisionMember
from ciudadfutura.utils import paginate
from .forms import LoginForm, UserForm, TagForm
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, RedirectView, TemplateView


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

    def get_context_data(self, **kwargs):
        ctx = super(RegisterView, self).get_context_data()
        ctx['page_title'] = 'Mision'
        return ctx


index = IndexView.as_view()
register = RegisterView.as_view()