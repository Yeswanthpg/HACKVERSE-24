# Generated by Django 5.0.6 on 2024-11-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experience_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('mentee', 'Mentee'), ('mentor', 'Mentor')], default='mentee', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
