from django.urls import path
from . import views
from .views import list_books, LibraryDetailView,Register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", list_books, name="index"),
    path("",LibraryDetailView.as_view(),name="details"),
    path("login/", LoginView.as_view(), name='login'),
    path("Register/", views.Register, name='register'),
    path("logout/", LogoutView.as_view(), name='logout'),

]