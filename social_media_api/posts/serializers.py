from rest_framework import serializers
from .models import Post,Comment


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = '__all__'

    

class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = '__all__'
    