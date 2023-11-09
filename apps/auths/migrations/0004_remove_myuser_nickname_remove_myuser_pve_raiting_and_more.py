# Generated by Django 4.2.7 on 2023-11-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_characters', '0002_character_pve_raiting_character_pvp_raiting'),
        ('auths', '0003_alter_myuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='pve_raiting',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='pvp_raiting',
        ),
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=1, max_length=200, verbose_name='никнейм'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='баланс'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='game_characters',
            field=models.ManyToManyField(blank=True, null=True, to='game_characters.character', verbose_name='ваши персонажи'),
        ),
    ]
