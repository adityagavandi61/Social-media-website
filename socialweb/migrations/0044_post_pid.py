# Generated by Django 3.2.23 on 2024-03-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0043_remove_post_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pid',
            field=models.IntegerField(default=1),
        ),
    ]
