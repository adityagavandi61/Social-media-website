# Generated by Django 3.2.23 on 2024-01-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0012_auto_20240129_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=250)),
                ('media', models.FileField(default=None, max_length=250, null=True, upload_to='posts/')),
            ],
        ),
        migrations.RemoveField(
            model_name='userregister',
            name='profile_pic',
        ),
    ]