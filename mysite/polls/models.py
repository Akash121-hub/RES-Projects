from pyexpat import model
from re import M
from turtle import update
from uuid import uuid4
import uuid
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# from django.db import models


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)

    class Meta:
        abstract = True


class Question(models.Model):
    question_text = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('date published', null=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='reverse_question')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Todo(BaseModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    todo_title = models.CharField(max_length=100)
    todo_desc = models.TextField()
    is_done = models.BooleanField(default=False)


class TimingTodo(BaseModel):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    timing = models.DateField()



