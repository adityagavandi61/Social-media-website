# Generated by Django 3.2.23 on 2024-03-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0090_likepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
