from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.DTOs.subscription_dto import SubscriptionResponseDto

@extend_schema(
    parameters=[
        OpenApiParameter(name="search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="status", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="planId", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="page", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="pageSize", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
    ],
    responses={200: SubscriptionResponseDto(many=True)}
)
@api_view(["GET"])
def subscription_list(request):
    return Response([
        {
            "id": "sub_1",
            "customerId": "cust_123",
            "planId": "plan_pro",
            "status": "Active",
            "price": 49.0
        }
    ])

@extend_schema(
    parameters=[OpenApiParameter(name="includeHistory", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY)],
    responses={200: SubscriptionResponseDto}
)
@api_view(["GET", "DELETE"])
def subscription_detail(request, subscriptionId):
    if request.method == "GET":
        return Response({
            "id": subscriptionId,
            "customerId": "cust_123",
            "planId": "plan_pro",
            "status": "Active",
            "price": 49.0
        })
    elif request.method == "DELETE":
        return Response({"message": f"Subscription '{subscriptionId}' cancelled successfully."}, status=status.HTTP_200_OK)
