# Generated by Django 3.0 on 2020-02-16 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0009_reports_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reports',
            old_name='user',
            new_name='added_by',
        ),
    ]