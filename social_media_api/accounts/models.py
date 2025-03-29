from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture =models.ImageField(upload_to=None)
    followers = models.ManyToManyField('self',symmetrical=False)
    following = models.ManyToManyField('self')
    def __str__(self):
        return self.email
    