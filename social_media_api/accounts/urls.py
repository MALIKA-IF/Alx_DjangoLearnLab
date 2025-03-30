from django.urls import path
from .views import register,Login,FollowApiView,unFollowApiView

urlpatterns = [
   
    path('register/',register.as_view(), name='register'),
    path('login/',Login, name='login'),
    path('follow/<int:user_id>/',FollowApiView.as_view, name='Follow'),
    path('unfollow/<int:user_id>/',unFollowApiView.as_view, name='unFollow'),
    


]
