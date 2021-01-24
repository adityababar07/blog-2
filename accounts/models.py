from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    standard = models.PositiveIntegerField(null=True, blank=True)
    division = models.CharField(max_length=1, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)



