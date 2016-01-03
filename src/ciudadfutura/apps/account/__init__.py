from django.apps import AppConfig


class Config(AppConfig):

    label = 'ciudadfutura_account'
    verbose_name = 'Mision Account'
    name = 'ciudadfutura.apps.account'
    models_module = 'ciudadfutura.apps.account.models'
