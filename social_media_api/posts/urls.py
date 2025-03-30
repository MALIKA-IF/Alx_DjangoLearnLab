from django.urls import path
from .views import FeedApiView

urlpatterns = [
    path('feed/',FeedApiView, name='feed'),
  
    

         
]