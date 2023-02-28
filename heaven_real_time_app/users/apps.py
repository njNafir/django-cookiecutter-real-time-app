from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "heaven_real_time_app.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import heaven_real_time_app.users.signals  # noqa F401
        except ImportError:
            pass
