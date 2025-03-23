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
    path('/post/', PostListView.as_view(template_name='listing.html'), name="PostList"),
    path('/post/new/', PostCreateView.as_view(template_name='creating.html'), name="NewPost"),
    path('/post/<int:pk>/', PostDetailView.as_view(template_name='viewing.html'), name="DetailPost"),
    path('/post/<int:pk>/update/', PostUpdateView.as_view(template_name='editing.html'), name="UpdatPost"),
    path('/post/<int:pk>/delete/', PostDeleteView.as_view(template_name='deleting.html'), name="DeletePost"),
    


]
