# Generated by Django 3.2.23 on 2024-03-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0129_auto_20240313_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
