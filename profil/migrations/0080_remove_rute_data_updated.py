# Generated by Django 4.1.7 on 2023-04-19 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0079_rute_data_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rute',
            name='data_updated',
        ),
    ]
