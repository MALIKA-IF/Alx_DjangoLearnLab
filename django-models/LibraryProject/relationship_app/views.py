from django.shortcuts import render
from django.http import HttpResponse
from.models import Book

# Create your views here.
def list_book(request):
    books=Book.objects.all()
    for book in books:
      return render(f"the title is {book.title} create by {book.author}")

def list(request):
     return render(request,'templates/list_books.html')
