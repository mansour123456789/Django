# Generated by Django 4.1.7 on 2023-04-20 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0090_ligne_modifier_id_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='ligne_modifier',
            name='id_condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.condition'),
        ),
    ]
