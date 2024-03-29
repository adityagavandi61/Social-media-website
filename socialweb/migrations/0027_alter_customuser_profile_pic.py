# Generated by Django 3.2.23 on 2024-02-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0026_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='static/assets/svg/profile.svg', upload_to='profilepic'),
        ),
    ]
