# Generated by Django 4.1.7 on 2023-04-20 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0087_remove_ligne_modifier_vieux_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ligne_modifier',
            name='Vieux',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
