from django.contrib import admin
from .models import employees, Post

# Register your models here.

admin.site.register(employees)
admin.site.register(Post)