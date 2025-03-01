from django.urls import path
from . import views
from .views import list_books, LibraryDetailView,RegisterView,Login,Logout


urlpatterns = [
    path("", list_books, name="index"),
    path("",LibraryDetailView.as_view(),name="details"),
    path("Login/", Login.as_view(), name='login'),
    path("RegisterView/", RegisterView.as_view(), name='register'),
    path("Logout/", Logout.as_view(), name='logout'),




]