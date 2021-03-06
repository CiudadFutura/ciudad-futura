from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from ciudadfutura.apps.auth.models import User, Tag, MisionMember
from ciudadfutura.apps.mision.models import Circle, Invite
from django.utils import timezone


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': 'autofocus',
        'placeholder': _('Email')
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': _('Password')
    }))

    def save(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        return auth.authenticate(username=email, password=password)


MAX_AGE = 150

now = timezone.now()

BIRTH_YEAR_CHOICES = [
    now.year - n for n in xrange(MAX_AGE)
]


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    invites = forms.IntegerField(widget=forms.HiddenInput(attrs={
        'max_count': 5, 'min_count': 2,
    }), required=False)

    class Meta:
        model = User
        exclude = [
            'created_at', 'updated_at', 'country', 'tags', 'relationships',
            'contribution', 'legacy', 'last_login', 'is_admin', 'is_staff',
            'password', 'username'
        ]
        widgets = {
            'birthdate': SelectDateWidget(years=BIRTH_YEAR_CHOICES),
        }

    class Media:
        js = (
            'mision/js/register.js',
        )

    def clean(self):

        invites = self.cleaned_data.get('invites', 0)
        if invites < 2:
            raise forms.ValidationError({'__all__': 'Minimo 2 miembros.'})

        if invites > 4:
            raise forms.ValidationError({'__all__': 'Maximo 5 miembros.'})

        return self.cleaned_data

    def save(self, commit=True):
        user = super(UserForm, self).save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save(update_fields=['password'])
        user.relationships.add(User.MISION)
        circle = Circle.objects.create()
        member = MisionMember.objects.create(
            user=user, is_lead=True, circle=circle
        )
        return member

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower()

        if not email:
            raise forms.ValidationError(_('This field is required.'))

        if email and User.objects.filter(email__iexact=email).count():
            raise forms.ValidationError('Email already exists.')
        return email


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = [
            'email', 'first_name', 'last_name'
        ]


class InviteRegisterForm(forms.ModelForm):

    def __init__(self,  *args, **kwargs):
        super(InviteRegisterForm, self).__init__(*args, **kwargs)
        self.fields['circle'] = forms.IntegerField(widget=forms.HiddenInput(),
                                                   initial=kwargs['initial'] if 'initial' in kwargs else {})

    class Meta:
        model = User
        exclude = [
            'created_at', 'updated_at', 'country', 'tags', 'relationships',
            'contribution', 'legacy', 'last_login', 'is_admin', 'is_staff',
            'username'
        ]
        widgets = {
            'birthdate': SelectDateWidget(years=BIRTH_YEAR_CHOICES)
        }

    def save(self, commit=True):
        user = super(InviteRegisterForm, self).save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save(update_fields=['password'])
        user.relationships.add(User.MISION)
        circle = Circle.objects.get(id=self.cleaned_data['circle'])
        member = MisionMember.objects.create(
            user=user, is_lead=False, circle=circle
        )
        return member

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower()

        if not email:
            raise forms.ValidationError({
                'email': _('This field is required.')
            })

        if email and User.objects.filter(email__iexact=email).count():
            raise forms.ValidationError('Email already exists.')
        return email


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = []
