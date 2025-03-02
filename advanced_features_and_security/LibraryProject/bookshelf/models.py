from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager



# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField()

class CustomUser(AbstractUser):
    date_of_birth=models.DateField()
    profile_photo=models.ImageField()    
#can_view, can_create, can_edit, and can_delete
    class Meta:
        permissions =[
            ("can_view","can view"),
            ("can_create","can create"),
            ("can_edit","can edit"),
             ("can_delete","can delete"),

        ]


class CustomUserManager(BaseUserManager):
    def create_user(self, email="None", password="None"):
        pass
    def create_superuser(self,email="None", password="None"):
        pass




