# Generated by Django 5.0.6 on 2024-11-27 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Unknown Location', max_length=100),
        ),
    ]
