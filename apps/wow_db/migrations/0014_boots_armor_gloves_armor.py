# Generated by Django 4.2.7 on 2023-11-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wow_db', '0013_alter_body_armor_required_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boots_armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('item_level', models.IntegerField(default=None, verbose_name='итемлевл')),
                ('quality', models.CharField(default=None, max_length=255, verbose_name='качество')),
                ('armor_type', models.CharField(default=None, max_length=255, verbose_name='тип брони')),
                ('armor', models.IntegerField(blank=True, default=None, null=True, verbose_name='броня')),
                ('strength', models.IntegerField(blank=True, default=None, null=True, verbose_name='сила')),
                ('stamina', models.IntegerField(blank=True, default=None, null=True, verbose_name='выносливость')),
                ('agility', models.IntegerField(blank=True, default=None, null=True, verbose_name='ловкость')),
                ('intelect', models.IntegerField(blank=True, default=None, null=True, verbose_name='интелект')),
                ('haste_rating', models.FloatField(blank=True, default=None, null=True, verbose_name='скорость')),
                ('crit_rating', models.FloatField(blank=True, default=None, null=True, verbose_name='крит')),
                ('versatility', models.FloatField(blank=True, default=None, null=True, verbose_name='универсальность')),
                ('mastery', models.FloatField(blank=True, default=None, null=True, verbose_name='искустность')),
                ('required_level', models.IntegerField(blank=True, default=None, null=True, verbose_name='уровень для экиперовки')),
                ('item_url', models.URLField(default=None, verbose_name='ссылка на предмет')),
                ('item_img', models.URLField(default=None, verbose_name='ссылка на изорбажение предмета')),
            ],
            options={
                'verbose_name': 'ботинки',
                'verbose_name_plural': 'ботинки',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Gloves_armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('item_level', models.IntegerField(default=None, verbose_name='итемлевл')),
                ('quality', models.CharField(default=None, max_length=255, verbose_name='качество')),
                ('armor_type', models.CharField(default=None, max_length=255, verbose_name='тип брони')),
                ('armor', models.IntegerField(blank=True, default=None, null=True, verbose_name='броня')),
                ('strength', models.IntegerField(blank=True, default=None, null=True, verbose_name='сила')),
                ('stamina', models.IntegerField(blank=True, default=None, null=True, verbose_name='выносливость')),
                ('agility', models.IntegerField(blank=True, default=None, null=True, verbose_name='ловкость')),
                ('intelect', models.IntegerField(blank=True, default=None, null=True, verbose_name='интелект')),
                ('haste_rating', models.FloatField(blank=True, default=None, null=True, verbose_name='скорость')),
                ('crit_rating', models.FloatField(blank=True, default=None, null=True, verbose_name='крит')),
                ('versatility', models.FloatField(blank=True, default=None, null=True, verbose_name='универсальность')),
                ('mastery', models.FloatField(blank=True, default=None, null=True, verbose_name='искустность')),
                ('required_level', models.IntegerField(blank=True, default=None, null=True, verbose_name='уровень для экиперовки')),
                ('item_url', models.URLField(default=None, verbose_name='ссылка на предмет')),
                ('item_img', models.URLField(default=None, verbose_name='ссылка на изорбажение предмета')),
            ],
            options={
                'verbose_name': 'ботинки',
                'verbose_name_plural': 'ботинки',
                'ordering': ('-id',),
            },
        ),
    ]
