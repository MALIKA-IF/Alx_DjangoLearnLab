from django.contrib.auth.views import LoginView,LogoutView
from .views import index,RegistrationView,profile
from .views import PostDeleteView,PostCreateView,PostDetailView,PostListView,PostUpdateView
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', RegistrationView.as_view(template_name='register.html'), name='register'),
    path('profile/', profile.as_view(template_name='profile.html'), name='profile'),
    path('list/', PostListView.as_view(template_name='Post_list.html'), name="PostList"),


]
