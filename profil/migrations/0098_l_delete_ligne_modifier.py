# Generated by Django 4.1.7 on 2023-04-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0097_ligne_modifier_delete_lignemodifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='l',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=50, null=True)),
                ('vieux', models.CharField(blank=True, max_length=50, null=True)),
                ('nouveau', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ligne_modifier',
        ),
    ]