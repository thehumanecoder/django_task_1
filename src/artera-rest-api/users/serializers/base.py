from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profiles

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profiles
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
    profile_handle = serializers.CharField(source='username', required=True, max_length=30)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'profile_handle']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value: str) -> str:
        """Django's built-in password validators."""
        try:
            validate_password(value)
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):

        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        # Create the profile with profile_handle and profile_picture
        Profiles.objects.update_or_create(user=user, defaults={
            'profile_handle': validated_data['username']
        })
        return user