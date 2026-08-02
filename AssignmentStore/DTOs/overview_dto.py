from rest_framework import serializers

class OverviewSummaryResponseDto(serializers.Serializer):
    totalRevenue = serializers.FloatField()
    totalOrders = serializers.IntegerField()
    totalCustomers = serializers.IntegerField()
    activeNow = serializers.IntegerField()
    currency = serializers.CharField(max_length=10)
