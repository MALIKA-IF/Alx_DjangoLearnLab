from django.shortcuts import render
from rest_framework import viewsets,generics,permissions
from .models import Post,Comment
from .serializers import Postserializer,Commentserializer
from accounts.models import CustomUser
from notifications.models import Notification
from rest_framework import generics,permissions
from .models import Like
from rest_framework.response import Response


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Commentserializer  

class FeedApiView(generics.GenericAPIView):
    serializer_class = Postserializer
    permission_classes=permissions.IsAuthenticated

    def get(self):
        following_users=Post.objects.filter(author__in=following_users).order_by('-created_at')
        following = following_users
        following.all()
        return following_users
    
class LikePost(generics.GenericAPIView):
    permission_classes=permissions.IsAuthenticated

    def like(self,pk,request):

        like=generics.get_object_or_404(Post,pk=pk)    
        if Like.objects.get_or_create(user=request.user, post=like):
            return Notification.objects.create
    
class unLikePost(generics.GenericAPIView):
    permission_classes=permissions.IsAuthenticated

    def unlike(self,pk,request,):

        unlike=generics.get_object_or_404(Post,pk=pk)    
        post=Like.objects.get_or_create(user=request.user, post=unlike)
        if not post:
            return Response({"You unliked this post."})
    
    
    
    
    
        


