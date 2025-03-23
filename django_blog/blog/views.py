from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout,login ,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import profile

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
    template_name = 'registration.html'


class profile(LoginRequiredMixin, DetailView):
    model = profile
    template_name = 'profile.html'  # Create this template
    context_object_name = 'profile'
