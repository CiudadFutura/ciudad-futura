from django.apps import AppConfig


class Config(AppConfig):

    label = 'ciudadfutura_order'
    verbose_name = 'Mision Order'
    name = 'ciudadfutura.apps.order'
    models_module = 'ciudadfutura.apps.order.models'
