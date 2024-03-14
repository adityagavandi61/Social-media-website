# Generated by Django 3.2.23 on 2024-03-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0134_sharepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharepost',
            old_name='user',
            new_name='username',
        ),
        migrations.AddField(
            model_name='post',
            name='no_of_share',
            field=models.IntegerField(default=0),
        ),
    ]
