from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomSerializer(serializers.ModelSerializer):
   class Meta :
        model = CustomUser
        fields = '__all__'

   def save(self):
         
         new_user=get_user_model().objects.create_user(
              username=serializers.CharField(),
              email=serializers.EmailField(),
              password=serializers.CharField(),
         )

         new_user.save()

         new_user=Token.objects.create(user=new_user)