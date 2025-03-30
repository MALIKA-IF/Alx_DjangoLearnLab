from django.urls import path
from .views import register,Login,FollowApiView

urlpatterns = [
   
    path('register/',register.as_view(), name='register'),
    path('login/',Login, name='login'),
    path('follow/<int:user_id>/',FollowApiView, name='Follow'),
    path('unfollow/<int:user_id>/',FollowApiView, name='unFollow'),
    


]
