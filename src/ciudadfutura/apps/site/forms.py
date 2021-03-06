from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from ciudadfutura.apps.auth.models import User
from django.utils import timezone

MAX_AGE = 150

now = timezone.now()

BIRTH_YEAR_CHOICES = [
    now.year - n for n in xrange(MAX_AGE)
]


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'dni',
            'birthdate',
            'city',
            'address',
            'postal_code',
        ]
        widgets = {
            'birthdate': SelectDateWidget(years=BIRTH_YEAR_CHOICES),
        }
