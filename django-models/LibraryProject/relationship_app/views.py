from django.shortcuts import render
from django.http import HttpResponse
from.models import Book, Library
from django.views import generic

# Create your views here.
Book.objects.all()

def index(request):

    return render(request,'relationship_app/list_books.html')

class Details(generic.DetailView):

    template_name = "relationship_app/library_detail.html"

    

    
    
