# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class User_PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=10, blank=False)
    #other fields here  

