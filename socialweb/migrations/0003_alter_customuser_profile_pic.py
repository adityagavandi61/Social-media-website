# Generated by Django 3.2.23 on 2024-02-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0002_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(upload_to='Gallery/profile_pic'),
        ),
    ]
