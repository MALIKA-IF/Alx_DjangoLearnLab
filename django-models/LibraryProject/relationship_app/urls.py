from django.urls import path
from . import views

urlpatterns = [

   path("list/", views.list_books, name="list"),
    path("library/",views.LibraryDetailView.as_view(),name="details"),
   # path("login/", views.LoginView, name='login'),
    path("Register/", views.Register.as_view, name='register'),
 #   path("logout/", views.LogoutView, name='logout'),

   path("add_book/",views.permission_required, name ="addBook"),
   path("edit_book/",views.permission_required, name ="editBook"),
   path("delete_book/",views.permission_required, name ="deleteBook"),
   

]
