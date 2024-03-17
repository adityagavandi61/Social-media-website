# Generated by Django 3.2.23 on 2024-03-16 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0143_auto_20240316_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='youtube',
        ),
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.URLField(null=True)),
                ('gmail', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('youtube', models.URLField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialweb.profile')),
            ],
        ),
    ]
