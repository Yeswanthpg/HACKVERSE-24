# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class User_PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=10, blank=False)
    #other fields here  


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # Unique identifier
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    skills = models.TextField(blank=True, null=True)  # Comma-separated or descriptive list of skills
    experience_level = models.PositiveIntegerField(help_text="Experience level in months")
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
