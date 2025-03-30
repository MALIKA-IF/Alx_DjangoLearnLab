from django.urls import path
from .models import Notification

urlpatterns = [

    path('notifications/',Notification, name='feed'),
    
]
