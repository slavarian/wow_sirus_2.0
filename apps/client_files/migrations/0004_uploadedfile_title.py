# Generated by Django 4.2.7 on 2023-12-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_files', '0003_uploadedfile_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='описание'),
            preserve_default=False,
        ),
    ]
