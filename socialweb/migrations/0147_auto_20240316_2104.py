# Generated by Django 3.2.23 on 2024-03-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0146_links_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='gmail',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
