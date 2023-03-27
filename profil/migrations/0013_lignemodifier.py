# Generated by Django 4.1.7 on 2023-03-17 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0012_alter_mansour_id_file_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='lignemodifier',
            fields=[
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.CharField(blank=True, max_length=50, null=True)),
                ('ligne', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='profil.mansour')),
                ('id_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.file')),
            ],
        ),
    ]
