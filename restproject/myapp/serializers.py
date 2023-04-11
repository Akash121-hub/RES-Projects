from asyncore import read
from rest_framework import serializers
from . models import Post, employees
from django import forms
# from .serializers import PostSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField(many=False,read_only=True)
    

    class Meta:
        model = Post
        fields = ('id','title','description','timestamp','created_by','created_on','file')


class employeesSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True,read_only=True)
    class Meta:
        model = employees
        fields = ('first_name', 'last_name','posts','posts_id')





class UserSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['username', 'password','first_name', 'last_name','user_posts','email']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class employeesSerializer(serializers.ModelSerializer):
    # employee_posts = PostSerializer(many=True,read_only=True)
    class Meta:
        model = employees
        fields = ('first_name', 'last_name')










