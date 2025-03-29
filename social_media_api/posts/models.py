from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='AuthorP')
    title=models.TextField()
    content=models.TextField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE) 
    authorC=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='authorCommet')
    content=models.TextField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()