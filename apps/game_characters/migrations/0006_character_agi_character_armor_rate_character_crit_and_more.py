# Generated by Django 4.2.7 on 2023-11-14 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_characters', '0005_game_specialization_game_class_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='agi',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ловкость'),
        ),
        migrations.AddField(
            model_name='character',
            name='armor_rate',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='броня'),
        ),
        migrations.AddField(
            model_name='character',
            name='crit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='крит'),
        ),
        migrations.AddField(
            model_name='character',
            name='haste_rating',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='скорость'),
        ),
        migrations.AddField(
            model_name='character',
            name='health',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='здоровье'),
        ),
        migrations.AddField(
            model_name='character',
            name='intellect',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='интелект'),
        ),
        migrations.AddField(
            model_name='character',
            name='mana',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='мана'),
        ),
        migrations.AddField(
            model_name='character',
            name='masteryy',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='исскустность'),
        ),
        migrations.AddField(
            model_name='character',
            name='stamina',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='выносливость'),
        ),
        migrations.AddField(
            model_name='character',
            name='str',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='сила'),
        ),
        migrations.AddField(
            model_name='character',
            name='versatility',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='универсальность'),
        ),
    ]
