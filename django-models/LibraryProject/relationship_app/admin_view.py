from .models import UserProfile
from django.shortcuts import render

def admin(request):
    return render(request, "admin_view.html")
