from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='AuthorP')
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    created_at=models.DateField()
    updated_at=models.DateField()

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE) 
    authorC=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='authorCommet')
    content=models.CharField(max_length=100)
    created_at=models.DateField()
    updated_at=models.DateField()