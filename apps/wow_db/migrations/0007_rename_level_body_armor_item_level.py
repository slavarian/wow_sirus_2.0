# Generated by Django 4.2.7 on 2023-11-13 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wow_db', '0006_body_armor_intelect_body_armor_mastery_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='body_armor',
            old_name='level',
            new_name='item_level',
        ),
    ]