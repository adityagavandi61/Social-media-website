# Generated by Django 3.2.23 on 2024-02-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0017_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'viewer'), (2, 'profile')], default=1),
        ),
    ]
