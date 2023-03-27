# Generated by Django 4.1.7 on 2023-03-22 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0018_filems_dv'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('fileid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.filems')),
            ],
        ),
    ]
