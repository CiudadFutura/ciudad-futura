from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from ciudadfutura.decorators import staff_required
from ciudadfutura.apps.auth.models import User, Tag, MisionMember
from ciudadfutura.utils import paginate
from .forms import LoginForm, UserForm, TagForm


def admin_logout(request):
    auth.logout(request)
    messages.success(request, _('You have successfully logged out.'))
    return redirect('adminpanel:login')


def admin_login(request):

    form = None

    if request.user.is_authenticated():
        return redirect('adminpanel:dashboard')

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None and user.is_active:
                auth.login(request, user)
                messages.success(request, _('Authentication succeed.'))
                return redirect(request.GET.get('next') or 'adminpanel:dashboard')

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
def admin_user_list(request):
    selected = [
        int(tag_id) for tag_id in request.GET.getlist('tags')
    ]

    results = User.objects.all()
    if selected:
        results = results.filter(tags__in=selected)

    return render(request, 'mision/admin_user_list.html', {
        'results': paginate(request.GET, results),
        'tags': Tag.objects.all(),
        'selected': selected
    })


@staff_required
def admin_user_form(request, user_id=None):

    user = None

    if user_id is not None:
        user = User.objects.get(id=user_id)

    if request.POST:
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('adminpanel:user-list')
    else:
        form = UserForm(instance=user)

    return render(request, 'mision/admin_user_form.html', {
        'form': form,
    })


@staff_required
def admin_user_details(request, user_id):
    return render(request, 'mision/admin_user_details.html', {})


@staff_required
def admin_user_delete(request, user_id):
    User.objects.get(id=user_id).delete()
    messages.success(request, _('User successfully deleted.'))
    return redirect('adminpanel:user-list')


@staff_required
def admin_tag_list(request):
    return render(request, 'mision/admin_tag_list.html', {
        'results': paginate(request.GET, Tag.objects.all())
    })


@staff_required
def admin_tag_delete(request, tag_id):
    Tag.objects.get(id=tag_id).delete()
    messages.success(request, _('Tag successfully deleted.'))
    return redirect('adminpanel:tag-list')


@staff_required
def admin_tag_form(request, tag_id=None):
    tag = None

    if tag_id is not None:
        tag = Tag.objects.get(id=tag_id)

    if request.POST:
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save()
            messages.success(request, _('Tag successfully saved.'))
            return redirect('adminpanel:tag-list')
    else:
        form = TagForm(instance=tag)

    return render(request, 'mision/admin_tag_form.html', {
        'form': form,
    })
