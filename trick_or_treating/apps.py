from django.apps import AppConfig
from django.db.models.signals import post_save


class TrickOrTreatingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "trick_or_treating"

    def ready(self):
        from .models import Address
        from .signals import prepare_address

        post_save.connect(prepare_address, sender=Address)
        return super().ready()
