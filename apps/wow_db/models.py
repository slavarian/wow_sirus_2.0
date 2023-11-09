from django.db import models



class Body_armor(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=200,
        unique= True
    )
    type_armor = models.CharField(
        verbose_name='тип брони',
        max_length=100,
        null=True,
        blank=True
    )
    
    armor_rate = models.IntegerField(
        verbose_name='рейтинг брони',
        null=True, blank=True
        
    )
    intelligence = models.IntegerField(
        verbose_name='интеллект',
        null=True, blank=True
    )
    strength = models.IntegerField(
        verbose_name='сила',
        null=True, blank=True
    )
    agility = models.IntegerField(
        verbose_name='сила',
        null=True, blank=True
    )
    equipment_level = models.IntegerField(
        verbose_name='требуемый уровень',
        null=True, blank=True 
    )
    
    item_level = models.IntegerField(
        verbose_name='уровень предмета',
        null=True, blank=True 
    )
    def __str__(self):
        return self.title

    class Meta:
        app_label = 'wow_db' 
