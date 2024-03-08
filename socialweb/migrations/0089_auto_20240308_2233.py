# Generated by Django 3.2.23 on 2024-03-08 17:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0088_auto_20240308_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_id',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
