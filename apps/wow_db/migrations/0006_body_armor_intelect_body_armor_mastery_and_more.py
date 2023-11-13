# Generated by Django 4.2.7 on 2023-11-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wow_db', '0005_remove_body_armor_armor_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='body_armor',
            name='intelect',
            field=models.IntegerField(default=None, verbose_name='интелект'),
        ),
        migrations.AddField(
            model_name='body_armor',
            name='mastery',
            field=models.FloatField(default=None, verbose_name='искустность'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='agility',
            field=models.IntegerField(default=None, verbose_name='ловкость'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='armor',
            field=models.IntegerField(default=None, verbose_name='броня'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='armor_type',
            field=models.CharField(default=None, max_length=255, verbose_name='тип брони'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='crit_rating',
            field=models.FloatField(default=None, verbose_name='крит'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='haste_rating',
            field=models.FloatField(default=None, verbose_name='скорость'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='item_url',
            field=models.URLField(default=None, verbose_name='ссылка на предмет'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='level',
            field=models.IntegerField(default=None, verbose_name='итемлевл'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='quality',
            field=models.CharField(default=None, max_length=255, verbose_name='качество'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='required_level',
            field=models.IntegerField(default=None, verbose_name='уровень для экиперовки'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='stamina',
            field=models.IntegerField(default=None, verbose_name='выносливость'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='strength',
            field=models.IntegerField(default=None, verbose_name='сила'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='title',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='body_armor',
            name='versatility',
            field=models.FloatField(default=None, verbose_name='универсальность'),
        ),
    ]
