from rest_framework import serializers

class CustomerUserRequestDto(serializers.Serializer):
    fullName = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=False, allow_blank=True)
    avatarUrl = serializers.CharField(max_length=500, required=False, allow_blank=True)
    role = serializers.CharField(max_length=50, default="Owner")

class CustomerUserResponseDto(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    fullName = serializers.CharField(max_length=100)
    avatarUrl = serializers.CharField(max_length=500, allow_blank=True)

class CreateCustomerRequestDto(serializers.Serializer):
    companyName = serializers.CharField(max_length=150)
    domain = serializers.CharField(max_length=150, required=False, allow_blank=True)
    status = serializers.CharField(max_length=50, default="Prospect")
    category = serializers.CharField(max_length=100, required=False, allow_blank=True)
    description = serializers.CharField(max_length=500, required=False, allow_blank=True)
    users = CustomerUserRequestDto(many=True, required=False, default=list)

class CustomerResponseDto(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    companyName = serializers.CharField(max_length=150)
    logoUrl = serializers.CharField(max_length=500, allow_blank=True)
    domain = serializers.CharField(max_length=150, allow_blank=True)
    status = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=100, allow_blank=True)
    description = serializers.CharField(max_length=500, allow_blank=True)
    userCount = serializers.IntegerField(default=0)
    users = CustomerUserResponseDto(many=True, default=list)
    createdAt = serializers.CharField(max_length=50)
    lastActiveAt = serializers.CharField(max_length=50)
