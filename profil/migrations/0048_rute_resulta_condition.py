# Generated by Django 4.1.7 on 2023-03-26 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0047_delete_condition_delete_resulta_delete_rute'),
    ]

    operations = [
        migrations.CreateModel(
            name='rute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='resulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=50, null=True)),
                ('mot', models.CharField(blank=True, max_length=50, null=True)),
                ('id_rute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.rute')),
            ],
        ),
        migrations.CreateModel(
            name='condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=50, null=True)),
                ('mot', models.CharField(blank=True, max_length=50, null=True)),
                ('id_rute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.rute')),
            ],
        ),
    ]
