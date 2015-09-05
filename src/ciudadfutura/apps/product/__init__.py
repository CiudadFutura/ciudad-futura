from django.apps import AppConfig


class Config(AppConfig):

    label = 'ciudadfutura_product'
    verbose_name = 'Mision Product'
    name = 'ciudadfutura.apps.product'
    models_module = 'ciudadfutura.apps.product.models'
