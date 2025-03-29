from django.shortcuts import render
from rest_framework import viewsets
from .models import Post,Comment
from .serializers import Postserializer,Commentserializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Commentserializer  