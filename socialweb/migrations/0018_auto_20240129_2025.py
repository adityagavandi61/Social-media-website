# Generated by Django 3.2.23 on 2024-01-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0017_remove_userregister_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='page_name',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='phone_number',
            field=models.CharField(default='default_value', max_length=15),
        ),
    ]