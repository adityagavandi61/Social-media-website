# Generated by Django 3.2.23 on 2024-03-03 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0053_post_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='socialweb.profile'),
        ),
    ]
