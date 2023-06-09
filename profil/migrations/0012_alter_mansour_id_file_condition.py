# Generated by Django 4.1.7 on 2023-03-17 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0011_mansour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mansour',
            name='id_file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.file'),
        ),
        migrations.CreateModel(
            name='condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(blank=True, max_length=50, null=True)),
                ('choix', models.CharField(blank=True, max_length=50, null=True)),
                ('id_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.file')),
            ],
        ),
    ]
