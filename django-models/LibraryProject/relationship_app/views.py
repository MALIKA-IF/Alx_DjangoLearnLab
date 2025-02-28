from django.shortcuts import render
from django.http import HttpResponse
from.models import Book

# Create your views here.
Book.objects.all()

def index(request):

    return render(request,'relationship_app/list_books.html')

