# Generated by Django 3.0 on 2019-12-11 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='gender',
            new_name='type',
        ),
    ]
