# Generated by Django 4.1.7 on 2023-04-19 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0070_remove_rute_imported_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rute',
            name='updated',
        ),
    ]