from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.core.signals import setting_changed


# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=20)

def __str__(self):
    return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  

def __str__(self):
    return self.title
   
    
class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book,related_name='library')
class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library,on_delete=models.CASCADE,related_name='librarian')

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    STATUS_Admin = ""
    STATUS_Librarian = ""
    STATUS_Member = ""
    STATUS_CHOICES = [
        (STATUS_Admin, 'Admin'),
        (STATUS_Librarian, 'Librarian'),
        (STATUS_Member, 'Member'),
    ]
    role = models.CharField(max_length=20 ,choices=STATUS_CHOICES)

setting_changed.connect(UserProfile)




