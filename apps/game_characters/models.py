from django.db import models
from django.utils import timezone
from wow_db.models import (Body_armor , Head_armor , Boots_armor ,
                           Gloves_armor , Legs_armor ,Back_armor,
                            Shoulder_armor , Wrist_armor , Belt_armor,
                            Ring , Trinket , Weapon , Amulet  )

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

class Armor_type(models.Model):
    title = models.CharField(
            verbose_name="тип брони",
            max_length=50
        )
    def __str__(self):
        return self.title

class Weapon_type(models.Model):
    title = models.CharField(
            verbose_name="тип оружия",
            max_length=50
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
    class_armor_type = models.ForeignKey(
        verbose_name='тип используемой экиперовки',
        to=Armor_type,
        on_delete=models.CASCADE
    )
    class_weapon_type = models.ManyToManyField(
        verbose_name='тип используемого оружия',
        to=Weapon_type
    )
    class_logo = models.ImageField(
        verbose_name='лого класса',
        upload_to='images/'
    )
    def __str__(self):
        return f"{self.title}({self.specialization.title})"



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
    head_armor = models.ForeignKey(
        verbose_name= 'нагудник',
        to=Head_armor,
        null=True, blank=True,
        on_delete=models.CASCADE
    )

    boots_armor = models.ForeignKey(
        verbose_name= 'ботинки',
        to=Boots_armor,
        null=True, blank=True,
        on_delete=models.CASCADE
    )
    gloves_armor = models.ForeignKey(
            verbose_name= 'ботинки',
            to=Gloves_armor,
            null=True, blank=True,
            on_delete=models.CASCADE
        )
    legs_armor = models.ForeignKey(
            verbose_name= 'ботинки',
            to=Legs_armor,
            null=True, blank=True,
            on_delete=models.CASCADE
        )
    back_armor = models.ForeignKey(
            verbose_name= 'ботинки',
            to=Back_armor,
            null=True, blank=True,
            on_delete=models.CASCADE
        )
    shoulder_armor = models.ForeignKey(
            verbose_name= 'ботинки',
            to=Shoulder_armor,
            null=True, blank=True,
            on_delete=models.CASCADE
        )
    wrist_armor = models.ForeignKey(
            verbose_name= 'ботинки',
            to=Wrist_armor,
            null=True, blank=True,
            on_delete=models.CASCADE
        )
    belt_armor = models.ForeignKey(
            verbose_name= 'ботинки',
            to=Belt_armor,
            null=True, blank=True,
            on_delete=models.CASCADE
        )
   
    amulet = models.ForeignKey(
            verbose_name= 'ботинки',
            to=Amulet,
            null=True, blank=True,
            on_delete=models.CASCADE
        )
    ring1 = models.ForeignKey(Ring, on_delete=models.CASCADE,
                              null=True, blank=True, related_name='кольцо_1')
    ring2 = models.ForeignKey(Ring, on_delete=models.CASCADE,
                              null=True, blank=True, related_name='кольцо_2')

    trinket1 = models.ForeignKey(Trinket, on_delete=models.CASCADE,
                                 null=True, blank=True, related_name='тринкет_1')
    trinket2 = models.ForeignKey(Trinket, on_delete=models.CASCADE,
                                 null=True, blank=True, related_name='тринкет_2')
    weapon1 = models.ForeignKey(Weapon, on_delete=models.CASCADE,
                                null=True, blank=True, related_name='left_hand_weapons')
    weapon2 = models.ForeignKey(Weapon, on_delete=models.CASCADE,
                                null=True, blank=True, related_name='right_hand_weapons')
    

 
 
    def equip_armor(self, armor_type, armor):
        if armor_type == 'body':
            self.body_armor = armor
        elif armor_type == 'head':
            self.head_armor = armor
        elif armor_type == 'boots':
            self.boots_armor = armor
        elif armor_type == 'gloves':
            self.gloves_armor = armor
        elif armor_type == 'legs':
            self.legs_armor = armor
        elif armor_type == 'back':
            self.back_armor = armor
        elif armor_type == 'shoulder':
            self.shoulder_armor = armor
        elif armor_type == 'wrist':
            self.wrist_armor = armor
        elif armor_type == 'belt':
            self.belt_armor = armor
        elif armor_type == 'ring1':
            self.ring1 = armor
        elif armor_type == 'ring2':
            self.ring2 = armor
        elif armor_type == 'amulet':
            self.amulet = armor
        elif armor_type == 'trinket1':
            self.trinket1 = armor
        elif armor_type == 'trinket2':
            self.trinket2 = armor
        elif armor_type == 'weapon1':
            self.weapon1 = armor
        elif armor_type == 'weapon2':
            self.weapon2 = armor


    @property
    def gear_score(self):
        total_item_level = 0
        
        if self.body_armor:
            total_item_level += self.body_armor.item_level
        
        if self.head_armor:
            total_item_level += self.head_armor.item_level
        
        if self.gloves_armor:
            total_item_level += self.gloves_armor.item_level

        if self.shoulder_armor:
            total_item_level += self.shoulder_armor.item_level

        if self.amulet:
            total_item_level += self.amulet.item_level

        if self.wrist_armor:
            total_item_level += self.wrist_armor.item_level

        if self.back_armor:
            total_item_level += self.back_armor.item_level

        if self.belt_armor:
            total_item_level += self.belt_armor.item_level

        if self.legs_armor:
            total_item_level += self.legs_armor.item_level

        if self.boots_armor:
            total_item_level += self.boots_armor.item_level

        if self.ring1:
            total_item_level += self.ring1.item_level

        if self.ring2:
            total_item_level += self.ring2.item_level

        if self.trinket1:
            total_item_level += self.trinket1.item_level
        
        if self.trinket2:
            total_item_level += self.trinket2.item_level

        if self.weapon1:
            total_item_level += self.weapon1.item_level

        if self.weapon2:
            total_item_level += self.weapon2.item_level

        return int(total_item_level/15)

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
        total_health = 50
    
        
        
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

        if self.head_armor:
            total_agility += self.head_armor.agility or 0
            total_strength += self.head_armor.strength or 0
            total_intellect += self.head_armor.intelect or 0
            total_stamina += self.head_armor.stamina or 0
            total_crit += self.head_armor.crit_rating or 0
            total_haste_rating += self.head_armor.haste_rating or 0
            total_versatility += self.head_armor.versatility or 0
            total_mastery += self.head_armor.mastery or 0
            total_armor_rating += self.head_armor.armor or 0

        if self.amulet:
            total_agility += self.amulet.agility or 0
            total_strength += self.amulet.strength or 0
            total_intellect += self.amulet.intelect or 0
            total_stamina += self.amulet.stamina or 0
            total_crit += self.amulet.crit_rating or 0
            total_haste_rating += self.amulet.haste_rating or 0
            total_versatility += self.amulet.versatility or 0
            total_mastery += self.amulet.mastery or 0
        
        if self.shoulder_armor:
            total_agility += self.shoulder_armor.agility or 0
            total_strength += self.shoulder_armor.strength or 0
            total_intellect += self.shoulder_armor.intelect or 0
            total_stamina += self.shoulder_armor.stamina or 0
            total_crit += self.shoulder_armor.crit_rating or 0
            total_haste_rating += self.shoulder_armor.haste_rating or 0
            total_versatility += self.shoulder_armor.versatility or 0
            total_mastery += self.shoulder_armor.mastery or 0
            total_armor_rating += self.shoulder_armor.armor or 0

        if self.shoulder_armor:
            total_agility += self.shoulder_armor.agility or 0
            total_strength += self.shoulder_armor.strength or 0
            total_intellect += self.shoulder_armor.intelect or 0
            total_stamina += self.shoulder_armor.stamina or 0
            total_crit += self.shoulder_armor.crit_rating or 0
            total_haste_rating += self.shoulder_armor.haste_rating or 0
            total_versatility += self.shoulder_armor.versatility or 0
            total_mastery += self.shoulder_armor.mastery or 0
            total_armor_rating += self.shoulder_armor.armor or 0

        if self.back_armor:
            total_agility += self.back_armor.agility or 0
            total_strength += self.back_armor.strength or 0
            total_intellect += self.back_armor.intelect or 0
            total_stamina += self.back_armor.stamina or 0
            total_crit += self.back_armor.crit_rating or 0
            total_haste_rating += self.back_armor.haste_rating or 0
            total_versatility += self.back_armor.versatility or 0
            total_mastery += self.back_armor.mastery or 0
            total_armor_rating += self.back_armor.armor or 0

        if self.wrist_armor:
            total_agility += self.wrist_armor.agility or 0
            total_strength += self.wrist_armor.strength or 0
            total_intellect += self.wrist_armor.intelect or 0
            total_stamina += self.wrist_armor.stamina or 0
            total_crit += self.wrist_armor.crit_rating or 0
            total_haste_rating += self.wrist_armor.haste_rating or 0
            total_versatility += self.wrist_armor.versatility or 0
            total_mastery += self.wrist_armor.mastery or 0
            total_armor_rating += self.wrist_armor.armor or 0

        if self.gloves_armor:
            total_agility += self.gloves_armor.agility or 0
            total_strength += self.gloves_armor.strength or 0
            total_intellect += self.gloves_armor.intelect or 0
            total_stamina += self.gloves_armor.stamina or 0
            total_crit += self.gloves_armor.crit_rating or 0
            total_haste_rating += self.gloves_armor.haste_rating or 0
            total_versatility += self.gloves_armor.versatility or 0
            total_mastery += self.gloves_armor.mastery or 0
            total_armor_rating += self.gloves_armor.armor or 0

        if self.belt_armor:
            total_agility += self.belt_armor.agility or 0
            total_strength += self.belt_armor.strength or 0
            total_intellect += self.belt_armor.intelect or 0
            total_stamina += self.belt_armor.stamina or 0
            total_crit += self.belt_armor.crit_rating or 0
            total_haste_rating += self.belt_armor.haste_rating or 0
            total_versatility += self.belt_armor.versatility or 0
            total_mastery += self.belt_armor.mastery or 0
            total_armor_rating += self.belt_armor.armor or 0

        if self.legs_armor:
            total_agility += self.legs_armor.agility or 0
            total_strength += self.legs_armor.strength or 0
            total_intellect += self.legs_armor.intelect or 0
            total_stamina += self.legs_armor.stamina or 0
            total_crit += self.legs_armor.crit_rating or 0
            total_haste_rating += self.legs_armor.haste_rating or 0
            total_versatility += self.legs_armor.versatility or 0
            total_mastery += self.legs_armor.mastery or 0
            total_armor_rating += self.legs_armor.armor or 0    
        
        if self.boots_armor:
            total_agility += self.boots_armor.agility or 0
            total_strength += self.boots_armor.strength or 0
            total_intellect += self.boots_armor.intelect or 0
            total_stamina += self.boots_armor.stamina or 0
            total_crit += self.boots_armor.crit_rating or 0
            total_haste_rating += self.boots_armor.haste_rating or 0
            total_versatility += self.boots_armor.versatility or 0
            total_mastery += self.boots_armor.mastery or 0
            total_armor_rating += self.boots_armor.armor or 0    

        if self.ring1:
            total_agility += self.ring1.agility or 0
            total_strength += self.ring1.strength or 0
            total_intellect += self.ring1.intelect or 0
            total_stamina += self.ring1.stamina or 0
            total_crit += self.ring1.crit_rating or 0
            total_haste_rating += self.ring1.haste_rating or 0
            total_versatility += self.ring1.versatility or 0
            total_mastery += self.ring1.mastery or 0
            
        if self.ring2:
            total_agility += self.ring2.agility or 0
            total_strength += self.ring2.strength or 0
            total_intellect += self.ring2.intelect or 0
            total_stamina += self.ring2.stamina or 0
            total_crit += self.ring2.crit_rating or 0
            total_haste_rating += self.ring2.haste_rating or 0
            total_versatility += self.ring2.versatility or 0
            total_mastery += self.ring2.mastery or 0
        
        if self.trinket1:
            total_agility += self.trinket1.agility or 0
            total_strength += self.trinket1.strength or 0
            total_intellect += self.trinket1.intelect or 0
            total_stamina += self.trinket1.stamina or 0
            total_crit += self.trinket1.crit_rating or 0
            total_haste_rating += self.trinket1.haste_rating or 0
            total_versatility += self.trinket1.versatility or 0
            total_mastery += self.trinket1.mastery or 0

        if self.trinket2:
            total_agility += self.trinket2.agility or 0
            total_strength += self.trinket2.strength or 0
            total_intellect += self.trinket2.intelect or 0
            total_stamina += self.trinket2.stamina or 0
            total_crit += self.trinket2.crit_rating or 0
            total_haste_rating += self.trinket2.haste_rating or 0
            total_versatility += self.trinket2.versatility or 0
            total_mastery += self.trinket2.mastery or 0

        return {
            'agility': total_agility,
            'strength': total_strength,
            'intellect': total_intellect,
            'stamina': total_stamina,
            'crit': int(total_crit)/100,
            'haste_rating': total_haste_rating/100,
            'versatility': total_versatility/100,
            'mastery': total_mastery/100,
            'armor_rating': total_armor_rating,
            'health': total_health*total_stamina
        }
    
    
