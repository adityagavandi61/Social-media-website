# Generated by Django 3.2.23 on 2024-01-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0030_auto_20240131_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='profile_pic',
            field=models.FileField(default='/static/assets\\img\\pp.webp', max_length=250, null=True, upload_to='profile_pic/'),
        ),
    ]
