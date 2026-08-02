from rest_framework import serializers

class SubscriptionResponseDto(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    customerId = serializers.CharField(max_length=100)
    planId = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=50)
    price = serializers.FloatField()
