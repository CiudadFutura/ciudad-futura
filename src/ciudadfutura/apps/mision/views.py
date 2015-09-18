from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from ciudadfutura.decorators import staff_required
from ciudadfutura.mixins import StaffMixin
from ciudadfutura.apps.auth.models import Person, Tag
from .forms import LoginForm, PersonForm, TagForm


def index(request):
    return render(request, 'mision/index.html', {
        'page_title': 'Mision',
    })


def register(request):

    return render(request, 'mision/register.html', {
        'page_title': 'Mision Register',
    })


def admin_logout(request):
    auth.logout(request)
    messages.success(request, _('You have successfully logged out.'))
    return redirect('admin-login')


def admin_login(request):

    form = None

    if request.user.is_authenticated():
        return redirect('admin-dashboard')

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None and user.is_active:
                auth.login(request, user)
                messages.success(request, _('Authentication succeed.'))
                return redirect(request.GET.get('next') or 'admin-dashboard')

        messages.error(request, _('Authentication failed.'))
    else:
        form = LoginForm()

    return render(request, 'mision/admin_login.html', {
        'form': form
    })


@staff_required
def admin_dashboard(request):
    return render(request, 'mision/admin_dashboard.html', {

    })


@staff_required
def admin_person_list(request):
    selected = [
        int(tag_id) for tag_id in request.GET.getlist('tags')
    ]

    results = Person.objects.all()
    if selected:
        results = results.filter(tags__in=selected)

    return render(request, 'mision/admin_person_list.html', {
        'results': results,
        'tags': Tag.objects.all(),
        'selected': selected
    })


@staff_required
def admin_person_form(request, person_id=None):

    person = None

    if person_id is not None:
        person = Person.objects.get(id=person_id)

    if request.POST:
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save()
            messages.success(request, _('Person successfully saved.'))
            return redirect('admin-person-list')
    else:
        form = PersonForm(instance=person)

    return render(request, 'mision/admin_person_form.html', {
        'form': form,
    })


@staff_required
def admin_person_details(request, person_id):
    return render(request, 'mision/admin_person_details.html', {})


@staff_required
def admin_person_delete(request, person_id):
    Person.objects.get(id=person_id).delete()
    messages.success(request, _('Person successfully deleted.'))
    return redirect('admin-person-list')


@staff_required
def admin_tag_list(request):
    return render(request, 'mision/admin_tag_list.html', {
        'results': Tag.objects.all()
    })


@staff_required
def admin_tag_delete(request, tag_id):
    Tag.objects.get(id=tag_id).delete()
    messages.success(request, _('Tag successfully deleted.'))
    return redirect('admin-tag-list')


@staff_required
def admin_tag_form(request, tag_id=None):
    tag = None

    if tag_id is not None:
        tag = Tag.objects.get(id=tag_id)

    if request.POST:
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save()
            messages.success(request, _('Person successfully saved.'))
            return redirect('admin-tag-list')
    else:
        form = TagForm(instance=tag)

    return render(request, 'mision/admin_tag_form.html', {
        'form': form,
    })
