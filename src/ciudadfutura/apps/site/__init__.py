from django.apps import AppConfig


class Config(AppConfig):

    label = 'ciudadfutura_site'
    verbose_name = 'Mision Site'
    name = 'ciudadfutura.apps.site'
    models_module = 'ciudadfutura.apps.site.models'
