from django.apps import AppConfig


class Config(AppConfig):

    label = 'ciudadfutura_mision'
    verbose_name = 'Mision Mision'
    name = 'ciudadfutura.apps.mision'
    models_module = 'ciudadfutura.apps.mision.models'
