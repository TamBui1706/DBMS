from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.DTOs.discount_dto import DiscountResponseDto

@extend_schema(
    parameters=[
        OpenApiParameter(name="search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="status", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="type", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="applicableTo", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="startsFrom", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="startsTo", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="expiresFrom", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="expiresTo", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="sort", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="page", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="pageSize", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
    ],
    responses={200: DiscountResponseDto(many=True)}
)
@api_view(["GET"])
def discount_list(request):
    return Response([
        {
            "id": "dsc_100",
            "code": "SUMMER20",
            "type": "Percentage",
            "value": 20.0,
            "status": "Active"
        }
    ])
