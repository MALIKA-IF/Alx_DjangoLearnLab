from django.shortcuts import render
from django.http import HttpResponse
from.models import Book

# Create your views here.


def index(request):
    return render(request,'relationship_app/list_books.html')

def index2(request):
    return render(request,'relationship_app/library_detail.html')
