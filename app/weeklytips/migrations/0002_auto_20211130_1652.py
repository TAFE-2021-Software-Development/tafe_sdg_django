# Generated by Django 3.2.9 on 2021-11-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weeklytips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SustainableTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Description', models.CharField(max_length=700)),
                ('DateAdded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='WeeklyTips',
        ),
    ]
