# Generated by Django 4.2.7 on 2023-11-07 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название класса')),
                ('class_logo', models.ImageField(upload_to='images/', verbose_name='лого класса')),
            ],
        ),
        migrations.CreateModel(
            name='Game_fraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название фракции')),
                ('fraction_logo', models.ImageField(upload_to='images/', verbose_name='лого фракции')),
            ],
        ),
        migrations.CreateModel(
            name='Game_race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название расы')),
                ('race_logo', models.ImageField(upload_to='images/', verbose_name='лого рассы')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=28, unique=True, verbose_name='никнейм')),
                ('character_level', models.IntegerField(blank=True, default=1, null=True, verbose_name='уровень персонажа')),
                ('fraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_characters.game_fraction', verbose_name='фракция')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_characters.game_race', verbose_name='расса')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_characters.game_class', verbose_name='класс')),
            ],
        ),
    ]