from django.db import models

from wow_db.models import Body_armor

class Game_class(models.Model):
    title = models.CharField(
        verbose_name= "название класса",
        max_length=50
    )
    class_logo = models.ImageField(
        verbose_name='лого класса',
        upload_to='images/'
    )
    def __str__(self):
        return self.title

class Game_fraction(models.Model):
    title = models.CharField(
        verbose_name= "название фракции",
        max_length=50
    )
    fraction_logo = models.ImageField(
        verbose_name='лого фракции',
        upload_to='images/'
    )
    def __str__(self):
        return self.title

class Game_race(models.Model):
    title = models.CharField(
        verbose_name= "название расы",
        max_length=50
    )
    race_logo = models.ImageField(
        verbose_name='лого рассы',
        upload_to='images/'
    )
    def __str__(self):
        return self.title


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
        to = Game_class,
        on_delete=models.CASCADE
    )

    fraction = models.ForeignKey(
        verbose_name='фракция',
        to = Game_fraction,
        on_delete=models.CASCADE
    )

    race = models.ForeignKey(
        verbose_name='расса',
        to = Game_race,
        on_delete=models.CASCADE
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

  

    body_armor = models.ForeignKey(
        verbose_name= 'нагудник',
        to=Body_armor,
        null=True, blank=True,
        on_delete=models.CASCADE
    )
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

