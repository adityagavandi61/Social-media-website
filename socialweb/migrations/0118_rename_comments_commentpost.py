# Generated by Django 3.2.23 on 2024-03-12 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialweb', '0117_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='CommentPost',
        ),
    ]