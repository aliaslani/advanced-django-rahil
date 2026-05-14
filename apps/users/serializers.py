from rest_framework import serializers
from django.contrib.auth import authenticate



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if not '@' in value:
            raise serializers.ValidationError('Email address is not valid')
        return value
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        if email and password:
            if email in password:
                raise serializers.ValidationError('Email address is not valid')
        else:
            raise serializers.ValidationError('Email address is not valid')
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_active:
            raise serializers.ValidationError('User is not active')
        data['user'] = user
        return data

