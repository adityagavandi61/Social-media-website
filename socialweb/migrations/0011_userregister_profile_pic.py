# Generated by Django 3.2.23 on 2024-01-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0010_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='profile_pic',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='posts/'),
        ),
    ]