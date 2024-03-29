# Generated by Django 3.2.23 on 2024-03-13 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0131_auto_20240313_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialweb.viewer'),
        ),
        migrations.AlterField(
            model_name='followerscount',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialweb.viewer'),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialweb.viewer'),
        ),
    ]
