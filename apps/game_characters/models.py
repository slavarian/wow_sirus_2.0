from django.db import models

class Game_class(models.Model):
    title = models.CharField(
        verbose_name= "название класса",
        max_length=50
    )
    class_logo = models.ImageField(
        verbose_name='лого класса',
        upload_to='images/'
    )

class Game_fraction(models.Model):
    title = models.CharField(
        verbose_name= "название фракции",
        max_length=50
    )
    fraction_logo = models.ImageField(
        verbose_name='лого фракции',
        upload_to='images/'
    )

class Game_race(models.Model):
    title = models.CharField(
        verbose_name= "название расы",
        max_length=50
    )
    race_logo = models.ImageField(
        verbose_name='лого рассы',
        upload_to='images/'
    )


class Character(models.Model):
    nick_name = models.CharField(
        verbose_name= "никнейм",
        max_length=28 , 
        unique= True
    )

    character_level = models.IntegerField(
        verbose_name='уровень персонажа',
        default= 1,
        null=True, blank=True
    )

    specialization = models.ForeignKey(
        verbose_name="класс",
        to = Game_class
    )

    fraction = models.ForeignKey(
        verbose_name='фракция',
        to = Game_fraction
    )

    race = models.ForeignKey(
        verbose_name='расса',
        to = Game_race
    )

    healmet = models.ForeignKey(
        verbose_name= 'шлем',
        to = ... ,
        null=True, blank=True
    )

    body_armor = models.ForeignKey(
        verbose_name= 'нагудник',
        to = ... ,
        null=True, blank=True
    )

    glows = models.ForeignKey(
        verbose_name= 'перчатки',
        to = ... ,
        null=True, blank=True
    )

    legs = models.ForeignKey(
        verbose_name= 'ноги',
        to = ... ,
        null=True, blank=True
    )

    boots = models.ForeignKey(
        verbose_name= 'обувь',
        to = ... ,
        null=True, blank=True
    )


