# Generated by Django 4.0.4 on 2022-06-16 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trombinoscoop', '0002_alter_personne_date_naissance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Formation',
            new_name='Cursus',
        ),
        migrations.RenameModel(
            old_name='Universite',
            new_name='Faculte',
        ),
        migrations.RenameField(
            model_name='etudiant',
            old_name='formation',
            new_name='cursus',
        ),
        migrations.RenameField(
            model_name='personne',
            old_name='universite',
            new_name='faculte',
        ),
    ]
