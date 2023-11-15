from django.contrib import admin

from .models import Character , Game_class  , Game_specialization
# Register your models here.

admin.site.register(Character)
admin.site.register(Game_class)


admin.site.register(Game_specialization)