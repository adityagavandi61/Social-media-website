# Generated by Django 3.2.23 on 2024-03-13 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0124_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.FileField(null=True, upload_to='profilepic'),
        ),
    ]
