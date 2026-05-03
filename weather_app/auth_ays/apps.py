from django.apps import AppConfig


class AuthAysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_ays'

    def ready(self):
        import auth_ays.signals
