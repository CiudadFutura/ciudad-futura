from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django import forms
from ciudadfutura.apps.auth.models import Person


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


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ['tags', 'created_at', 'updated_at']
