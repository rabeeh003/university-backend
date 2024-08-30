from rest_framework import serializers # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import College

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['user', 'profile', 'place', 'phone', 'district', 'panchayath', 'latitude', 'longitude', 'description', 'is_active']
        depth = 1