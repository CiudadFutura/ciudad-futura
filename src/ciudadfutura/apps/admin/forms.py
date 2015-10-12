from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from ciudadfutura.apps.auth.models import User, Tag, Supplier
from ciudadfutura.apps.product.models import Product
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

    class Meta:
        model = User
        exclude = [
            'created_at',
            'updated_at',
            'country',
            'last_login',
            'username',
            'password',
            'legacy'
        ]
        widgets = {
            'birthdate': SelectDateWidget(years=BIRTH_YEAR_CHOICES),
            'relationships': forms.CheckboxSelectMultiple,
            'tags': forms.CheckboxSelectMultiple,
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower()
        if email and User.objects.filter(email__iexact=email).count():
            raise forms.ValidationError('Email already exists.')
        return email


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = []


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class SupplierForm(forms.ModelForm):

    # default_zones = forms.CharField()

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'postal_code', 'city', 'telephone', 'cellphone', 'address'
        ]

    def save(self, commit=True):

        user = super(SupplierForm, self).save(commit)
        supplier = Supplier.objects.create(
            user=user
        )
        return supplier



