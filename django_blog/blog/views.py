from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout,login ,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import profile,Post
from django.views.generic import DetailView,ListView,DeleteView,CreateView,UpdateView

# Create your views here.

def index(request):
    return render(request,'blog/base.html')

def logout_view(request):
    logout(request)

def Login_View(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return "good"
    else:
        return "login faild"
    
class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()



class profile(LoginRequiredMixin, DetailView):
    model = profile
    template_name = 'profile.html'  # Create this template
    context_object_name = 'profile'


class PostDetailView(DetailView):

  model = Post
  template_name = 'blog/Post_detail.html'

class PostListView(ListView):
    model = Post
    template_name = "blog/Post_list.html" 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create_Post.html"
    fields = ["title", "content"]

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "update_Post.html"
    fields = ["title", "content"]    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "delete_Post.html"    