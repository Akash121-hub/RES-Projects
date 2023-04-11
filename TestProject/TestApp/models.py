from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = (('Survey', 'Survey'),
    ('Discussion','Discussion'),
    ('Diary','Diary'))
    title = models.CharField(max_length=100, blank=True)
    order = models.CharField(max_length=100, blank=True, null=True)