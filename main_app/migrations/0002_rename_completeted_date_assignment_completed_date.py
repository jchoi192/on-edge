# Generated by Django 3.2.5 on 2021-07-22 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='completeted_date',
            new_name='completed_date',
        ),
    ]
