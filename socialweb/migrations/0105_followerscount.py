# Generated by Django 3.2.23 on 2024-03-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0104_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
