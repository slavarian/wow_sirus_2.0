# Generated by Django 4.2.7 on 2023-12-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_files', '0004_uploadedfile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='heading',
            field=models.CharField(default=1, max_length=255, verbose_name='заголовок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='title',
            field=models.TextField(verbose_name='описание'),
        ),
    ]
