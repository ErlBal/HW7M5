import random
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import VerificationCode


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=255, write_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('id', 'username', 'password')
       extra_kwargs = {
           'password': {'write_only': True}
       }

class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationCode
        fields = ('code',)



