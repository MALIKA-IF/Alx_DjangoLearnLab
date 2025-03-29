from django.urls import path
from .views import register,Login

urlpatterns = [
   
    path('register/',register.as_view(), name='register'),
    path('login/',Login, name='login'),
]
