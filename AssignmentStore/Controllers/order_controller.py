from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.Services.order_service import OrderService
from AssignmentStore.DTOs.order_dto import (
    CreateOrderRequestDto, UpdateOrderRequestDto, UpdateOrderStatusRequestDto, OrderResponseDto
)

order_service = OrderService()

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
        customer_id = request.query_params.get("customerId")
        status_val = request.query_params.get("status")
        data = order_service.list_orders(customer_id=customer_id, status=status_val)
        return Response(OrderResponseDto(data, many=True).data)
    elif request.method == "POST":
        serializer = CreateOrderRequestDto(data=request.data)
        if serializer.is_valid():
            created = order_service.create_order(
                customer_id=serializer.validated_data["customerId"],
                total_amount=serializer.validated_data["totalAmount"],
                items=serializer.validated_data.get("items", [])
            )
            return Response(OrderResponseDto(created).data, status=status.HTTP_201_CREATED)
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
        data = order_service.get_order(orderId)
        if not data:
            return Response({"detail": f"Order '{orderId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(OrderResponseDto(data).data)
    elif request.method == "PUT":
        serializer = UpdateOrderRequestDto(data=request.data)
        if serializer.is_valid():
            data = order_service.get_order(orderId)
            if not data:
                return Response({"detail": f"Order '{orderId}' not found."}, status=status.HTTP_404_NOT_FOUND)
            return Response(OrderResponseDto(data).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        success = order_service.delete_order(orderId)
        if not success:
            return Response({"detail": f"Order '{orderId}' not found."}, status=status.HTTP_404_NOT_FOUND)
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
        updated = order_service.update_order_status(orderId, serializer.validated_data["status"])
        if not updated:
            return Response({"detail": f"Order '{orderId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(OrderResponseDto(updated).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

