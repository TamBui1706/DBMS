from rest_framework import serializers

class LoginRequestDto(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

class RegisterRequestDto(serializers.Serializer):
    fullName = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

class LogoutRequestDto(serializers.Serializer):
    refreshToken = serializers.CharField(max_length=500, required=False, allow_blank=True)

class RefreshTokenRequestDto(serializers.Serializer):
    refreshToken = serializers.CharField(max_length=500)

class AuthResponseDto(serializers.Serializer):
    accessToken = serializers.CharField(max_length=500)
    refreshToken = serializers.CharField(max_length=500)
    tokenType = serializers.CharField(max_length=50, default="Bearer")

class UserMeResponseDto(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    fullName = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    role = serializers.CharField(max_length=50)
    store = serializers.JSONField(required=False, default=dict)
