from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
user = get_user_model()

class Author (models.Model):
    name=models.CharField(max_length=20)

def __str__(self):
    return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    
def __str__(self):
    return self.title
   
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  
class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book,related_name='library')
class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library,on_delete=models.CASCADE)
