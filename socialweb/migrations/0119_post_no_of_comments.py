# Generated by Django 3.2.23 on 2024-03-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0118_rename_comments_commentpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_of_comments',
            field=models.IntegerField(default=0),
        ),
    ]
