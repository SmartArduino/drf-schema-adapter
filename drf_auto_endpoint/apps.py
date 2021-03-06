from importlib import import_module

from django.apps import AppConfig
from django.conf import settings as django_settings
from django.utils.module_loading import autodiscover_modules


class DRFAutoEndpointConfig(AppConfig):
    name = 'drf_auto_endpoint'

    def ready(self):
        from .router import router
        autodiscover_modules('endpoints', register_to=router)
