from django.contrib import admin
from .models import (Body_armor , Head_armor , Boots_armor ,
                           Gloves_armor , Legs_armor ,Back_armor,
                            Shoulder_armor , Wrist_armor , Belt_armor,
                            Ring , Trinket , Weapon , Amulet  )
# Register your models here.

admin.site.register(Body_armor)
admin.site.register(Head_armor)
admin.site.register(Boots_armor)
admin.site.register(Gloves_armor)
admin.site.register(Legs_armor)
admin.site.register(Back_armor)
admin.site.register(Shoulder_armor)
admin.site.register(Wrist_armor)
admin.site.register(Belt_armor)
admin.site.register(Ring)
admin.site.register(Trinket)
admin.site.register(Amulet)
admin.site.register(Weapon)
