# Generated by Django 3.2.23 on 2024-02-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0036_post_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.IntegerField(),
        ),
    ]