# Generated by Django 4.2.7 on 2023-11-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wow_db', '0020_alter_weapon_max_damage_alter_weapon_min_damage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='attack_speed',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True, verbose_name='скорость 1 удара'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='damage_per_second',
            field=models.DecimalField(blank=True, decimal_places=1, default=None, max_digits=5, null=True, verbose_name='урон за секунду'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='max_damage',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='максимальный урон'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='min_damage',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='минимальный урон'),
        ),
    ]
