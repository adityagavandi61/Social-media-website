# Generated by Django 3.2.23 on 2024-03-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0052_auto_20240303_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.IntegerField(default=1),
        ),
    ]