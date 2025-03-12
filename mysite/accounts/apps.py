from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """This is the default login system bundled with Django."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
