# Generated by Django 4.1.7 on 2023-04-19 02:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0075_rute_imported_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='rute',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]