from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Character

@receiver(pre_save, sender=Character)
def validate_race(sender, instance, **kwargs):
    # Определите ограничения для выбора расс в зависимости от фракции
    if instance.fraction.title == 'Орда' and instance.race.title not in ['орк']:
        raise ValidationError('Неподходящая расса для фракции Орда')
    elif instance.fraction.title == 'Альянс' and instance.race.title not in ['Человек']:
        raise ValidationError('Неподходящая расса для фракции Альянс')
