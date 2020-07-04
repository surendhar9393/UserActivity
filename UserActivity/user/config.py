from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'UserActivity.user'

    def ready(self):
        pass

