from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.DTOs.order_dto import (
    CreateOrderRequestDto, UpdateOrderRequestDto, UpdateOrderStatusRequestDto, OrderResponseDto
)

@extend_schema(
    parameters=[
        OpenApiParameter(name="search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="customerId", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="status", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="paymentStatus", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="fulfillmentStatus", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="createdFrom", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="createdTo", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="minTotal", type=OpenApiTypes.NUMBER, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="maxTotal", type=OpenApiTypes.NUMBER, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="sort", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="page", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="pageSize", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
    ],
    request=CreateOrderRequestDto,
    responses={200: OrderResponseDto(many=True), 201: OrderResponseDto}
)
@api_view(["GET", "POST"])
def order_list(request):
    if request.method == "GET":
        return Response([
            {
                "id": "ord_1001",
                "customerId": "cust_123",
                "totalAmount": 250.0,
                "status": "Completed",
                "paymentStatus": "Paid",
                "fulfillmentStatus": "Fulfilled",
                "items": [{"productId": "prd_1", "quantity": 2, "price": 125.0}]
            }
        ])
    elif request.method == "POST":
        serializer = CreateOrderRequestDto(data=request.data)
        if serializer.is_valid():
            return Response({
                "id": "ord_1002",
                "customerId": serializer.validated_data["customerId"],
                "totalAmount": serializer.validated_data["totalAmount"],
                "status": "Pending",
                "paymentStatus": "Unpaid",
                "fulfillmentStatus": "Unfulfilled",
                "items": serializer.validated_data.get("items", [])
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    parameters=[
        OpenApiParameter(name="includeItems", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="includeCustomer", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="includePayments", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="includeHistory", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
    ],
    request=UpdateOrderRequestDto,
    responses={200: OrderResponseDto}
)
@api_view(["GET", "PUT", "DELETE"])
def order_detail(request, orderId):
    if request.method == "GET":
        return Response({
            "id": orderId,
            "customerId": "cust_123",
            "totalAmount": 250.0,
            "status": "Completed",
            "paymentStatus": "Paid",
            "fulfillmentStatus": "Fulfilled",
            "items": []
        })
    elif request.method == "PUT":
        serializer = UpdateOrderRequestDto(data=request.data)
        if serializer.is_valid():
            return Response({
                "id": orderId,
                "customerId": "cust_123",
                "totalAmount": serializer.validated_data.get("totalAmount", 250.0),
                "status": serializer.validated_data.get("status", "Completed"),
                "paymentStatus": "Paid",
                "fulfillmentStatus": "Fulfilled",
                "items": []
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        return Response({"message": f"Order '{orderId}' deleted successfully."}, status=status.HTTP_200_OK)

@extend_schema(
    parameters=[OpenApiParameter(name="notifyCustomer", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY)],
    request=UpdateOrderStatusRequestDto,
    responses={200: OrderResponseDto}
)
@api_view(["PATCH"])
def order_status(request, orderId):
    serializer = UpdateOrderStatusRequestDto(data=request.data)
    if serializer.is_valid():
        return Response({
            "id": orderId,
            "customerId": "cust_123",
            "totalAmount": 250.0,
            "status": serializer.validated_data["status"],
            "paymentStatus": "Paid",
            "fulfillmentStatus": "Fulfilled",
            "items": []
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
