# Generated by Django 4.0.4 on 2022-06-22 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_last_name_user_nom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nom',
            new_name='last_name',
        ),
    ]
