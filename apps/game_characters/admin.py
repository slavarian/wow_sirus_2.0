from django.contrib import admin

from .models import Character , Game_class , Game_specialization , Armor_type , Weapon_type
# Register your models here.

admin.site.register(Character)
admin.site.register(Game_class)
admin.site.register(Game_specialization)
admin.site.register(Armor_type)
admin.site.register(Weapon_type)

