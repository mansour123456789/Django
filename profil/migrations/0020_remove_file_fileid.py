# Generated by Django 4.1.7 on 2023-03-22 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0019_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='fileid',
        ),
    ]