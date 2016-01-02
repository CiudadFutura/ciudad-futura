from django import forms
from django.forms.extras.widgets import SelectDateWidget
from ciudadfutura.apps.auth.models import User
from ciudadfutura.apps.mision.models import Circle
from django.utils import timezone
from floppyforms import ClearableFileInput

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
            'email'
        ]
        widgets = {
            'birthdate': SelectDateWidget(years=BIRTH_YEAR_CHOICES),
        }


class ImageThumbnailFileInput(ClearableFileInput):
    template_name = 'site/image_thumbnail.html'


class UserPublicProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'avatar'
        ]
        widgets = {
            'avatar': ImageThumbnailFileInput
        }


class MyCircleForm(forms.ModelForm):

    class Meta:
        model = Circle
        exclude = []
