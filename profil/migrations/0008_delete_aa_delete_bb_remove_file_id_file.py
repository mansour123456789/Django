# Generated by Django 4.1.7 on 2023-03-16 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0007_aa_bb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='aa',
        ),
        migrations.DeleteModel(
            name='bb',
        ),
        migrations.RemoveField(
            model_name='file',
            name='id_file',
        ),
    ]
