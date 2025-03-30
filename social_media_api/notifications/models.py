from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Notification(models.Model):
    recipient=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='recipient')
    actor=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='actor')
    verb=models.TextField()
    target=models.CharField(max_length=100)
    timestamp=models.TimeField()