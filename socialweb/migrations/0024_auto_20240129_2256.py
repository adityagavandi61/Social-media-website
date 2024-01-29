# Generated by Django 3.2.23 on 2024-01-29 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0023_userregister_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='caption',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userregister',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]