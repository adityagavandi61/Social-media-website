# Generated by Django 3.2.23 on 2024-03-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0083_auto_20240306_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.FileField(null=True, upload_to='profilepic'),
        ),
    ]
