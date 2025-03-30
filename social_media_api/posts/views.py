from django.shortcuts import render
from rest_framework import viewsets,generics,permissions
from .models import Post,Comment
from .serializers import Postserializer,Commentserializer
from accounts.models import CustomUser


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
        following_user=Post.objects.filter(author__in=following_user).order_by('-created_at')
        following = following_user
        following.all()
        return following_user
    

    
    
    
    
        


