# Generated by Django 4.1.7 on 2023-03-26 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0042_alter_rute_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resulta',
            name='code_C',
        ),
    ]
