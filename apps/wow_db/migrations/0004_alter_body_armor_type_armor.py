# Generated by Django 4.2.7 on 2023-11-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wow_db', '0003_alter_body_armor_type_armor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body_armor',
            name='type_armor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='тип брони'),
        ),
    ]
