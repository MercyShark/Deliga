from rest_framework import serializers

from apps.user_profile.models import UserProfile
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'username',
                  'date_of_birth', 'password', 'password2')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                "Password and confirm Password doesn't match")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user = user)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('email', 'password')

    extra_kwargs = {
        'email': {
            'write_only': True
        },
        'password': {
            'write_only': True
        }
    }

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','full_name','username','date_of_birth')

class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs


class UserCheckEmailAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class UserCheckUsernameAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
