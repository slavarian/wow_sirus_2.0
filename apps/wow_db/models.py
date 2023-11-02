from django.db import models

# Create your models here.

class Body_armor(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=200
    )
    armor_rate = models.IntegerField(
        verbose_name='рейтинг брони',
        
    )
    intelligence = models.IntegerField(
        verbose_name='интеллект',
    )
    strength =  models.IntegerField(
        verbose_name='интеллект',
    )

