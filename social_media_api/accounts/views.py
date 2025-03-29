from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .serializers import CustomSerializer

# Create your views here.


def Login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return "good"
    else:
        return "login faild"    
    
class register(CreateView):
    
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def registerform(request):
        serializer = CustomSerializer(data=request.data)
        if request.method == "POST":
            form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()    