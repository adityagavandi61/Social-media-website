# Generated by Django 3.2.23 on 2024-03-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0087_auto_20240308_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
