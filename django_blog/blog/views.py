from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout,login ,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'blog/base.html')

def logout_view(request):
    logout(request)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return "good"
    else:
        return "login faild"
    
def RegistrationForm(request):

    email = forms.EmailField()

    class Meta:
        model=User
        fields=['title','content','published_date','author']


