# Generated by Django 3.2.9 on 2021-11-22 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0002_auto_20211122_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicmodel',
            old_name='name',
            new_name='title',
        ),
    ]