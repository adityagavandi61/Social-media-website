# Generated by Django 3.2.23 on 2024-02-15 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0032_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
