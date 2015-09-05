from django.apps import AppConfig


class Config(AppConfig):

    label = 'ciudadfutura_cart'
    verbose_name = 'Mision Cart'
    name = 'ciudadfutura.apps.cart'
    models_module = 'ciudadfutura.apps.cart.models'
