from rest_framework import serializers

class CreateOrderRequestDto(serializers.Serializer):
    customerId = serializers.CharField(max_length=100)
    totalAmount = serializers.FloatField()
    items = serializers.ListField(child=serializers.JSONField(), required=False, default=list)

class UpdateOrderRequestDto(serializers.Serializer):
    totalAmount = serializers.FloatField(required=False)
    status = serializers.CharField(max_length=50, required=False)

class UpdateOrderStatusRequestDto(serializers.Serializer):
    status = serializers.CharField(max_length=50)
    notifyCustomer = serializers.BooleanField(default=True)

class OrderResponseDto(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    customerId = serializers.CharField(max_length=100)
    totalAmount = serializers.FloatField()
    status = serializers.CharField(max_length=50)
    paymentStatus = serializers.CharField(max_length=50)
    fulfillmentStatus = serializers.CharField(max_length=50)
    items = serializers.ListField(child=serializers.JSONField(), default=list)
