from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.DTOs.store_dto import UpdateStoreRequestDto, StoreResponseDto

@extend_schema(
    tags=["Store"],
    parameters=[
        OpenApiParameter(name="includeOwner", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="includeSettings", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
    ],
    request=UpdateStoreRequestDto,
    responses={200: StoreResponseDto}
)
@api_view(["GET", "PUT"])
def store_detail(request):
    if request.method == "GET":
        return Response({
            "id": "str_1001",
            "name": "My Online Store",
            "domain": "myonlinestore.com",
            "logoUrl": "https://example.com/logo.png",
            "currency": "USD",
            "owner": {"fullName": "Sophia Munn", "email": "sophia@untitledui.com"}
        })
    elif request.method == "PUT":
        serializer = UpdateStoreRequestDto(data=request.data)
        if serializer.is_valid():
            return Response({
                "id": "str_1001",
                "name": serializer.validated_data["name"],
                "domain": serializer.validated_data.get("domain", "myonlinestore.com"),
                "logoUrl": "https://example.com/logo.png",
                "currency": serializer.validated_data.get("currency", "USD"),
                "owner": {"fullName": "Sophia Munn", "email": "sophia@untitledui.com"}
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["Store"],
    parameters=[OpenApiParameter(name="replaceExisting", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY)],
    responses={200: StoreResponseDto}
)
@api_view(["POST"])
def store_logo(request):
    return Response({
        "id": "str_1001",
        "name": "My Online Store",
        "domain": "myonlinestore.com",
        "logoUrl": "https://example.com/new_logo.png",
        "currency": "USD"
    })
