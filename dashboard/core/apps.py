import os

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        if not os.environ.get('RUN_MAIN', None) or os.environ.get('RUN_MAIN') == 'true':
            from .mqtt_client import run_mqtt_client_in_thread
            run_mqtt_client_in_thread()
