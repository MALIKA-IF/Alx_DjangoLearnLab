from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout,login ,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import profile,Post
from django.views.generic import DetailView,ListView,DeleteView,CreateView,UpdateView
from .forms import PostForm

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
    template_name = 'profile.html'  
    context_object_name = 'profile'


class PostDetailView(DetailView):

     model = Post
     template_name = 'blog/viewing.html'

     def PostDetail(request, idPost):
        post = get_object_or_404(Post, id=idPost)
        return render(request, 'blog/detail.html', {'post': post})


class PostListView(ListView):
    model = Post
    template_name = "blog/listing.html" 

    def blog_list(request):
       posts = Post.objects.all()
       return render(request, 'blog/listing.html', {'posts': posts})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/creating.html"
    fields = ["title", "content"]

    def blog_create(request):
        if request.method == 'POST':
           form = PostForm(request.POST)
           if form.is_valid():
            form.save()
            


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "editing.html"
    fields = ["title", "content"]   

    def Post_edit(request, Postid):
             post = get_object_or_404(Post, id=Postid)
             if request.method == 'POST':
                form = PostForm(request.POST)
                if form.is_valid():
                   form.save()
           

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "deleting.html"    
    def blog_delete(request, Postid):
        post = get_object_or_404(Post, id=Postid)
        post.delete()