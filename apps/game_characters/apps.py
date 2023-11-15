from django.apps import AppConfig


class GameCharactersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game_characters'

    def ready(self):
        import game_characters.signals