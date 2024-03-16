# Generated by Django 3.2.23 on 2024-03-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0137_auto_20240316_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='gmail',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]
