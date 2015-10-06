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

    class Meta:
        model = User
        exclude = [
            'created_at', 'updated_at', 'country', 'tags', 'relationships', 'contribution',
            'legacy', 'last_login', 'is_admin', 'is_staff', 'password'
        ]
        widgets = {
            'birthdate': SelectDateWidget(years=BIRTH_YEAR_CHOICES),
        }


    def save(self, commit=True):
        user = super(UserForm, self).save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save(update_fields=['password'])
        user.relationships.add(User.MISION)
        # TODO: validate if the user has or not circle or if is coordinador (is_lead) and send the email
        circle = Circle.objects.create()
        member = MisionMember.objects.create(user=user, is_lead=True, circle=circle)
        return member

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower()
        if email and User.objects.filter(email__iexact=email).count():
            raise forms.ValidationError('Email already exists.')
        return email


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = [
            'email', 'first_name', 'last_name'
        ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = []
