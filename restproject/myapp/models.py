from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='owner')
    
    created_by = models.IntegerField(default = None,blank=True,null=True)
    created_on = models.DateTimeField(default=None,blank=True,null=True)
    file = models.FileField(blank=True, null=True)

class employees(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    posts = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    # emp_Id = models.IntegerField()

    def __str__(self):
        return self.first_name



    