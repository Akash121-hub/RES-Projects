from statistics import mode
from django.db import models

# Create your models here.

class Office(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Employee(models.Model):
    genders = [("M","male"),
    ("F","Female")]
    office = models.ForeignKey(Office,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=20,choices=genders)
