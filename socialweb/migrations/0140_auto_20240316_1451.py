# Generated by Django 3.2.23 on 2024-03-16 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0139_auto_20240316_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialweb.profile'),
        ),
    ]
