from rest_framework import serializers
from .models import MyUser
from rest_framework.exceptions import ValidationError

from rest_framework.serializers import (ModelSerializer,CharField)


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'date_of_birth', 'is_active', 'is_admin', 'user_role')


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'date_of_birth')

    def validate_email(self, value):
        if MyUser.objects.filter(email=value).exists():
            raise ValidationError("Email already exists")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        return value

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user