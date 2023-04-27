# Generated by Django 4.1.7 on 2023-04-21 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0098_l_delete_ligne_modifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='lignemodifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=50, null=True)),
                ('vieux', models.CharField(blank=True, max_length=50, null=True)),
                ('nouveau', models.CharField(blank=True, max_length=50, null=True)),
                ('id_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.condition')),
                ('id_ligne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.filems')),
            ],
        ),
        migrations.DeleteModel(
            name='l',
        ),
    ]
