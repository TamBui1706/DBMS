from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.DTOs.overview_dto import OverviewSummaryResponseDto

@extend_schema(
    tags=["Dashboard"],
    parameters=[
        OpenApiParameter(name="from", type=OpenApiTypes.DATE, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="to", type=OpenApiTypes.DATE, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="timezone", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="currency", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
    ],
    responses={200: OverviewSummaryResponseDto}
)

@api_view(["GET"])
def overview_summary(request):
    return Response({
        "totalRevenue": 128450.0,
        "totalOrders": 1420,
        "totalCustomers": 8468,
        "activeNow": 316,
        "currency": "USD"
    })
