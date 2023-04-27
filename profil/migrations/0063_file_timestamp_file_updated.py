# Generated by Django 4.1.7 on 2023-04-19 01:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0062_remove_file_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
