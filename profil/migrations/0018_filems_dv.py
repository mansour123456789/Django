# Generated by Django 4.1.7 on 2023-03-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0017_filems_delai_sec1_filems_uq0'),
    ]

    operations = [
        migrations.AddField(
            model_name='filems',
            name='dv',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
