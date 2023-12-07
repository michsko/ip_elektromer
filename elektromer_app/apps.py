from django.apps import AppConfig


class ElektromerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elektromer_app'


    def ready(self):
    	import elektromer_app.signals

