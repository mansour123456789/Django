# Generated by Django 4.1.7 on 2023-04-22 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0107_l_delete_lignemodifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='lm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=50, null=True)),
                ('vieux', models.CharField(blank=True, max_length=50, null=True)),
                ('nouveau', models.CharField(blank=True, max_length=50, null=True)),
                ('id_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.condition')),
                ('id_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.file')),
                ('id_ligne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.filems')),
            ],
        ),
        migrations.DeleteModel(
            name='l',
        ),
    ]
