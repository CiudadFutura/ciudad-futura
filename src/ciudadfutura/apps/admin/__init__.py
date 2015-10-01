from django.apps import AppConfig


class Config(AppConfig):

    label = 'ciudadfutura_admin'
    verbose_name = 'Mision Admin'
    name = 'ciudadfutura.apps.admin'
    models_module = 'ciudadfutura.apps.admin.models'
