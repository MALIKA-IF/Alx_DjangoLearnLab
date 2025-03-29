from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class CustomSerializer(serializers.ModelSerializer):
   class Meta :
        model = CustomUser
        fields = '__all__'

   def save(self):
         new_user=User.objects.create_user(
              username=self.validated_data['username'],
              email=self.validated_data['email'],
              password=self.validated_data['password'],
         )

         new_user.save()

         new_user=Token.objects.create(user=new_user)