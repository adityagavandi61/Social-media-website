# Generated by Django 3.2.23 on 2024-01-29 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0016_auto_20240129_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='profile_pic',
        ),
    ]
