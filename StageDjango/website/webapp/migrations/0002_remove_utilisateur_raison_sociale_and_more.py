# Generated by Django 4.0.4 on 2022-06-21 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='raison_sociale',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='representant',
        ),
    ]
