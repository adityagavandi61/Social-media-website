# Generated by Django 3.2.23 on 2024-01-22 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0002_auto_20240122_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewerregister',
            old_name='email',
            new_name='gmail',
        ),
    ]