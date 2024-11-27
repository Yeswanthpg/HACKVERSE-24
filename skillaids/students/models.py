from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class userdetails(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=12)
    user_type = models.CharField(max_length=255)

class Volunteer(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    skills = models.TextField()  # A comma-separated string of skills
    experience_level = models.IntegerField()  # Experience in months
    location = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    