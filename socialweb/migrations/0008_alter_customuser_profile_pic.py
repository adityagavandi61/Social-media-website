# Generated by Django 3.2.23 on 2024-02-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0007_remove_customuser_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.FileField(upload_to='Gallery/profile_pic'),
        ),
    ]
