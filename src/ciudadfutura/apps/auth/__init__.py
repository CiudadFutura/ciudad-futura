from django.apps import AppConfig


class Config(AppConfig):

    label = 'ciudadfutura_auth'
    verbose_name = 'Mision Auth'
    name = 'ciudadfutura.apps.auth'
    models_module = 'ciudadfutura.apps.auth.models'
