# Generated by Django 4.1.7 on 2023-03-23 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0031_alter_filems_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filems',
            name='file_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.file'),
        ),
    ]
