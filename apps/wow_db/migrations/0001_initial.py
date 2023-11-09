# Generated by Django 4.2.7 on 2023-11-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Body_armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('armor_rate', models.IntegerField(verbose_name='рейтинг брони')),
                ('intelligence', models.IntegerField(verbose_name='интеллект')),
                ('strength', models.IntegerField(verbose_name='интеллект')),
            ],
        ),
    ]