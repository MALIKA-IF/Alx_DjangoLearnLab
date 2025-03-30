from django.urls import path
from .views import FeedApiView,LikePost,unLikePost

urlpatterns = [
    path('feed/',FeedApiView.as_view, name='feed'),
    path('posts/<int:pk>/like/',LikePost.as_view, name='like'),
    path('posts/<int:pk>/unlike/',unLikePost.as_view, name='unlike'),
         
]