# Generated by Django 4.1.7 on 2023-04-20 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0086_ligne_modifier_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ligne_modifier',
            name='Vieux',
        ),
        migrations.RemoveField(
            model_name='ligne_modifier',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ligne_modifier',
            name='id_condition',
        ),
        migrations.RemoveField(
            model_name='ligne_modifier',
            name='id_file',
        ),
        migrations.RemoveField(
            model_name='ligne_modifier',
            name='nouveau',
        ),
    ]
