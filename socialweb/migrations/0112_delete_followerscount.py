# Generated by Django 3.2.23 on 2024-03-10 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0111_remove_followerscount_follower'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
    ]