from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



# Create your views here.
Book.objects.all()

def list_books(request):

    return render(request,'relationship_app/list_books.html')

class LibraryDetailView(DetailView):

    template_name = "relationship_app/library_detail.html"

class Register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = "relationship_app/register.html"


    
