from django.db import models



class Body_armor(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="название")
    item_level = models.IntegerField( default=None,
                             verbose_name="итемлевл")
    quality = models.CharField(max_length=255 ,  default=None,
                             verbose_name="качество")
    armor_type = models.CharField(max_length=255 , default=None,
                             verbose_name="тип брони")
    armor = models.IntegerField(default=None,
                             verbose_name="броня",
                             blank=True,null=True)
    strength = models.IntegerField( default=None,
                             verbose_name="сила",
                             blank=True,null=True)
    stamina = models.IntegerField( default=None,
                             verbose_name="выносливость",
                             blank=True,null=True)
    agility = models.IntegerField( default=None,
                             verbose_name="ловкость",
                             blank=True,null=True)
    intelect = models.IntegerField( default=None,
                             verbose_name="интелект",
                             blank=True,null=True)
    haste_rating = models.FloatField( default=None,
                             verbose_name="скорость",
                             blank=True,null=True)
    crit_rating = models.FloatField(default=None,
                             verbose_name="крит",
                             blank=True,null=True)
    versatility = models.FloatField( default=None,
                             verbose_name="универсальность",
                             blank=True,null=True)
    mastery = models.FloatField( default=None,
                             verbose_name="искустность",
                             blank=True,null=True)
    required_level = models.IntegerField( default=None,
                             verbose_name="уровень для экиперовки",
                              blank=True,null=True)
    item_url = models.URLField( default=None,
                             verbose_name="ссылка на предмет")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'нагрудник'
        verbose_name_plural = 'нагрудники'

class Head_armor(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="название")
    item_level = models.IntegerField( default=None,
                             verbose_name="итемлевл")
    quality = models.CharField(max_length=255 ,  default=None,
                             verbose_name="качество")
    armor_type = models.CharField(max_length=255 , default=None,
                             verbose_name="тип брони")
    armor = models.IntegerField(default=None,
                             verbose_name="броня",
                             blank=True,null=True)
    strength = models.IntegerField( default=None,
                             verbose_name="сила",
                             blank=True,null=True)
    stamina = models.IntegerField( default=None,
                             verbose_name="выносливость",
                             blank=True,null=True)
    agility = models.IntegerField( default=None,
                             verbose_name="ловкость",
                             blank=True,null=True)
    intelect = models.IntegerField( default=None,
                             verbose_name="интелект",
                             blank=True,null=True)
    haste_rating = models.FloatField( default=None,
                             verbose_name="скорость",
                             blank=True,null=True)
    crit_rating = models.FloatField(default=None,
                             verbose_name="крит",
                             blank=True,null=True)
    versatility = models.FloatField( default=None,
                             verbose_name="универсальность",
                             blank=True,null=True)
    mastery = models.FloatField( default=None,
                             verbose_name="искустность",
                             blank=True,null=True)
    required_level = models.IntegerField( default=None,
                             verbose_name="уровень для экиперовки",
                              blank=True,null=True)
    item_url = models.URLField( default=None,
                             verbose_name="ссылка на предмет")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'шлем'
        verbose_name_plural = 'шлема'
