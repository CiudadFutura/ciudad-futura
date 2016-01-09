from django import forms
from ciudadfutura.apps.order.models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = []
