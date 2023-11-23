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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'шлем'
        verbose_name_plural = 'шлема'

class Boots_armor(models.Model):
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'ботинки'
        verbose_name_plural = 'ботинки'

class Gloves_armor(models.Model):
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'ботинки'
        verbose_name_plural = 'ботинки'

class Legs_armor(models.Model):
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Штаны'
        verbose_name_plural = 'Штаны'

class Back_armor(models.Model):
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Плащ'
        verbose_name_plural = 'Плащи'

class Shoulder_armor(models.Model):
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Наплечник'
        verbose_name_plural = 'Наплечники'

class Wrist_armor(models.Model):
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Запястье'
        verbose_name_plural = 'Запястье'

class Belt_armor(models.Model):
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Пояс'
        verbose_name_plural = 'Пояса'

class Ring(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="название")
    item_level = models.IntegerField( default=None,
                             verbose_name="итемлевл")
    quality = models.CharField(max_length=255 ,  default=None,
                             verbose_name="качество")
    armor_type = models.CharField(max_length=255 , default=None,
                             verbose_name="тип брони")
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Кольцо'
        verbose_name_plural = 'Кольца'


class Amulet(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="название")
    item_level = models.IntegerField( default=None,
                             verbose_name="итемлевл")
    quality = models.CharField(max_length=255 ,  default=None,
                             verbose_name="качество")
    armor_type = models.CharField(max_length=255 , default=None,
                             verbose_name="тип брони")
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'амулет'
        verbose_name_plural = 'амулеты'

class Trinket(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="название")
    item_level = models.IntegerField( default=None,
                             verbose_name="итемлевл")
    quality = models.CharField(max_length=255 ,  default=None,
                             verbose_name="качество")
    armor_type = models.CharField(max_length=255 , default=None,
                             verbose_name="тип брони")
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
    enique_spell = models.CharField(
        max_length=255, default=None,
                            verbose_name="уникальная способность предмета"
    )
    required_level = models.IntegerField( default=None,
                             verbose_name="уровень для экиперовки",
                              blank=True,null=True)
    item_url = models.URLField( default=None,
                             verbose_name="ссылка на предмет")
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'


class Weapon(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="название")
    item_level = models.IntegerField( default=None,
                             verbose_name="итемлевл")
    quality = models.CharField(max_length=255 ,  default=None,
                             verbose_name="качество")
    waepon_type = models.CharField(max_length=255 , default=None,
                             verbose_name="тип брони")
    min_damage = models.IntegerField( default=None,
                             verbose_name="минимальный урон",
                             blank=True,null=True)
    max_damage = models.IntegerField( default=None,
                             verbose_name="максимальный урон",
                             blank=True,null=True)
    damage_per_second = models.IntegerField( default=None,
                             verbose_name="урон за секунду",
                             blank=True,null=True)
    attack_speed = models.IntegerField( default=None,
                             verbose_name="скорость 1 удара",
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
    item_img = models.URLField( default=None,
                             verbose_name="ссылка на изорбажение предмета")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'оружие'
        verbose_name_plural = 'оружия'
