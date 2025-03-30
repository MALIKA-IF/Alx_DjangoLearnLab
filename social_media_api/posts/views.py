from django.shortcuts import render
from rest_framework import viewsets,generics,permissions
from .models import Post,Comment
from .serializers import Postserializer,Commentserializer


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
        following=Post.objects.filter(author__in=following).order_by('-created_at')
        return following.all()
    
        


