from tabnanny import verbose
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fm.core'
    verbose_name = 'Controle de estações FM'
