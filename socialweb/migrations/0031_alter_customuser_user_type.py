# Generated by Django 3.2.23 on 2024-02-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0030_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'viewer'), (2, 'profile')], default=1, max_length=255),
        ),
    ]
