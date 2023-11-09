from django.contrib import admin

from .models import Character , Game_class , Game_fraction , Game_race
# Register your models here.

admin.site.register(Character)
admin.site.register(Game_class)
admin.site.register(Game_fraction)
admin.site.register(Game_race)