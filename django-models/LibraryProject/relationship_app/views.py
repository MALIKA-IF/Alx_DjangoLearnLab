from django.shortcuts import render
from django.http import HttpResponse
from.models import Book

# Create your views here.
#def list_book(request):
#   books=Book.objects.all()
#   return render(f"the title is {books.title} create by {books.author}")

def index(request):
    return render(request,'relationship_app/list_books.html')
