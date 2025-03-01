from django.urls import path
from . import views
from .views import list_books, LibraryDetailView,Register,Login,Logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", list_books, name="index"),
    path("",LibraryDetailView.as_view(),name="details"),
    path("login/", LoginView.as_view(), name='login'),
    path("register/", views.Register, name='register'),
    path("logout/", LogoutView.as_view(), name='logout'),


#views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="

]