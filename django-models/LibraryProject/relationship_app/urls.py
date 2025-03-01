from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("", list_books, name="index"),
    path("",LibraryDetailView.as_view(),name="details")


]