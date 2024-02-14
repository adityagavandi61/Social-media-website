# Generated by Django 3.2.23 on 2024-02-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0013_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(blank=True, choices=[(1, 'profile'), (2, 'viewer')], max_length=10),
        ),
    ]
