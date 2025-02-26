from django.contrib import admin
from django.urls import path
from .views import list, list_book

urlpatterns = [
    path('admin/', admin.site.urls),
   

]