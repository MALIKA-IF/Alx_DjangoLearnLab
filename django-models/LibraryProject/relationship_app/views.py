from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
Book.objects.all()

def list_books(request):

    return render(request,'relationship_app/list_books.html')

class LibraryDetailView(DetailView):

    template_name = "relationship_app/library_detail.html"

    

    
    
