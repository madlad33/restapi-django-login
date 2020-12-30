from rest_framework import serializers
from .models import *

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing the api view """
    name = serializers.CharField(max_length=50)


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model=UserProfile
        fields=['id','email','name','password']
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self,validated_data):
        """Create and return a new user"""
        user=UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']


        )
        return user

