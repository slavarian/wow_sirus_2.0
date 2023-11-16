from django.db import models
from django.utils import timezone
from wow_db.models import Body_armor

class Game_specialization(models.Model):
    title = models.CharField(
        verbose_name= "название подкласса",
        max_length=50
    )
    class_logo = models.ImageField(
        verbose_name='лого подкласса',
        upload_to='images/'
    )
    def __str__(self):
        return self.title

class Game_class(models.Model):
    title = models.CharField(
        verbose_name= "название класса",
        max_length=50
    )
    specialization = models.ForeignKey(
        verbose_name="подкласс",
        to=Game_specialization,
        on_delete=models.CASCADE
    )

    class_logo = models.ImageField(
        verbose_name='лого класса',
        upload_to='images/'
    )
    def __str__(self):
        return self.title



class Character(models.Model):
    class Genders(models.TextChoices):
        MALE = 'Male','Мужчина'
        FEMALE =  'Female','Женщина'

    class Game_races(models.TextChoices):
        Orc = 'Orc','Орк'
        Human =  'Human','Человек'
        Bood_elf ='Bood Elf','Эльф крови'
        Night_elf ='Night Elf','Ночной эльф'
        Goblin ='Goblin','Гоблин'
        Tauren ='Tauren','Корова'
        Troll ='Troll','Троль'
        Undead = 'Undead','Нежить'
        Pandaren= 'Pandaren','Панда'
        Gnome = 'Gnome','Гном'
        Dwarf= 'Dwarf','Дворф'
        Draeneir= 'Draeneir','Дреней'
        Worgen = 'Worgen','Ворген'
        
    class Game_fraction(models.TextChoices):
        Horde = 'Horde', 'Орда'
        Alliance = 'Alliance', 'Альянс'

    user = models.ForeignKey('auths.MyUser', on_delete=models.CASCADE)
    
    nick_name = models.CharField(
        verbose_name= "никнейм",
        max_length=28 , 
        unique= True
    )
    gender = models.CharField(
        verbose_name='пол персонажа',
        max_length=22,
        choices=Genders.choices,
        default=Genders.MALE
    )
    character_level = models.IntegerField(
        verbose_name='уровень персонажа',
        default= 70,
        null=True, blank=True
    )

    specialization = models.ForeignKey(
        verbose_name="класс",
        to = Game_class,
        on_delete=models.CASCADE
    )
    fraction = models.CharField(
        verbose_name='фракция',
        max_length=22,
        choices=Game_fraction.choices ,
        default=Game_fraction.Horde
    )

    race = models.CharField(
        verbose_name='расса',
        max_length=22,
        choices=Game_races.choices,
        default=Game_races.Orc
    )
    
    pvp_raiting = models.DecimalField(
        verbose_name='пвп рейтинг',
        max_digits=11,
        decimal_places=2,
        default=0
    )

    pve_raiting = models.DecimalField(
        verbose_name='пве рейтинг',
        max_digits=11,
        decimal_places=2,
        default=0
    )
    str = models.IntegerField(
        verbose_name='сила',
        default=0,
        null=True, blank=True,
    )
    stamina =  models.IntegerField(
        verbose_name='выносливость',
        default=0,
        null=True, blank=True,
    )
    intellect = models.IntegerField(
        verbose_name='интелект',
        default=0,
        null=True, blank=True,
    )
    agi = models.IntegerField(
        verbose_name='ловкость',
        default=0,
        null=True, blank=True,
    )
    crit =  models.IntegerField(
        verbose_name='крит',
        default=0,
        null=True, blank=True,
    )
    haste_rating= models.IntegerField(
        verbose_name='скорость',
        default=0,
        null=True, blank=True,
    )
    versatility = models.IntegerField(
        verbose_name='универсальность',
        default=0,
        null=True, blank=True,
    )
    masteryy = models.IntegerField(
        verbose_name='исскустность',
        default=0,
        null=True, blank=True,
    )
    armor_rate = models.IntegerField(
        verbose_name='броня',
        default=0,
        null=True, blank=True,
    )
    health = models.IntegerField(
        verbose_name='здоровье',
        default=100,
        null=True, blank=True,
    )
    mana = models.IntegerField(
        verbose_name='мана',
        default=100,
        null=True, blank=True,
    )
    damage = models.IntegerField(
        verbose_name='Урон',
        default=0,
        null=True, blank=True,
    )
    magical_damage = models.IntegerField(
        verbose_name='Магический урон',
        default=0,
        null=True, blank=True,
    )

    body_armor = models.ForeignKey(
        verbose_name= 'нагудник',
        to=Body_armor,
        null=True, blank=True,
        on_delete=models.CASCADE
    )
 
   
    def equip_body_armor(self, body_armor):
        self.body_armor = body_armor
        self.save()
    

    @property
    def gear_score(self):
        total_item_level = 0
        
        if self.body_armor:
            total_item_level += self.body_armor.item_level
        
        # if self.helmet:
        #     total_item_level += self.helmet.item_level
        
        # if self.gloves:
        #     total_item_level += self.gloves.item_level

        return total_item_level

    @property
    def total_stats(self):
        total_agility = 0
        total_strength = 0
        total_intellect = 0
        total_stamina = 0
        total_crit = 0
        total_haste_rating = 0
        total_versatility = 0
        total_mastery = 0
        total_armor_rating = 0
        
        
        if self.body_armor:
            total_agility += self.body_armor.agility or 0
            total_strength += self.body_armor.strength or 0
            total_intellect += self.body_armor.intelect or 0
            total_stamina += self.body_armor.stamina or 0
            total_crit += self.body_armor.crit_rating or 0
            total_haste_rating += self.body_armor.haste_rating or 0
            total_versatility += self.body_armor.versatility or 0
            total_mastery += self.body_armor.mastery or 0
            total_armor_rating += self.body_armor.armor or 0
  

        return {
            'agility': total_agility,
            'strength': total_strength,
            'intellect': total_intellect,
            'stamina': total_stamina,
            'crit': total_crit,
            'haste_rating': total_haste_rating,
            'versatility': total_versatility,
            'mastery': total_mastery,
            'armor_rating': total_armor_rating,
        }

    # def __str__(self):
    #     return self.nick_name
    
    # healmet = models.ForeignKey(
    #     verbose_name= 'шлем',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )


    # glows = models.ForeignKey(
    #     verbose_name= 'перчатки',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )

    # legs = models.ForeignKey(
    #     verbose_name= 'ноги',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )

    # boots = models.ForeignKey(
    #     verbose_name= 'обувь',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )

    # ring1 = models.ForeignKey(
    #     verbose_name= 'кольцо1',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )

    # ring2 = models.ForeignKey(
    #     verbose_name= 'кольцо2',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )

    # trinket1 = models.ForeignKey(
    #     verbose_name= 'тринькет1',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )

    # trinket2 = models.ForeignKey(
    #     verbose_name= 'тринькет2',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )

    # amulet =  models.ForeignKey(
    #     verbose_name= 'амулет',
    #     to = ... ,
    #     null=True, blank=True,
    #     on_delete=models.CASCADE
    # )


    # gear_score PropertyField

