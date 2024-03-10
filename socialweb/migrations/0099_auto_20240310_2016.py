# Generated by Django 3.2.23 on 2024-03-10 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0098_auto_20240310_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='socialweb.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
