from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.Services.product_service import ProductService
from AssignmentStore.DTOs.product_dto import CreateProductRequestDto, UpdateProductRequestDto, ProductResponseDto

product_service = ProductService()

@extend_schema(
    parameters=[
        OpenApiParameter(name="search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="status", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="type", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="categoryId", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="minPrice", type=OpenApiTypes.NUMBER, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="maxPrice", type=OpenApiTypes.NUMBER, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="stockStatus", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="createdFrom", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="createdTo", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="sort", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="page", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="pageSize", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
    ],
    request=CreateProductRequestDto,
    responses={200: ProductResponseDto(many=True), 201: ProductResponseDto}
)
@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        search = request.query_params.get("search")
        category_id = request.query_params.get("categoryId")
        data = product_service.list_products(search=search, category_id=category_id)
        return Response(ProductResponseDto(data, many=True).data)
    elif request.method == "POST":
        serializer = CreateProductRequestDto(data=request.data)
        if serializer.is_valid():
            created = product_service.create_product(
                name=serializer.validated_data["name"],
                price=serializer.validated_data["price"],
                category_id=serializer.validated_data.get("categoryId", ""),
                type_name=serializer.validated_data.get("type", "Physical"),
                stock_status=serializer.validated_data.get("stockStatus", "InStock")
            )
            return Response(ProductResponseDto(created).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    parameters=[
        OpenApiParameter(name="includeImages", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="includeVariants", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="includeStatistics", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
    ],
    request=UpdateProductRequestDto,
    responses={200: ProductResponseDto}
)
@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, productId):
    if request.method == "GET":
        data = product_service.get_product(productId)
        if not data:
            return Response({"detail": f"Product '{productId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(ProductResponseDto(data).data)
    elif request.method == "PUT":
        serializer = UpdateProductRequestDto(data=request.data)
        if serializer.is_valid():
            data = product_service.get_product(productId)
            if not data:
                return Response({"detail": f"Product '{productId}' not found."}, status=status.HTTP_404_NOT_FOUND)
            return Response(ProductResponseDto(data).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        success = product_service.delete_product(productId)
        if not success:
            return Response({"detail": f"Product '{productId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Product '{productId}' deleted successfully."}, status=status.HTTP_200_OK)


@extend_schema(
    parameters=[
        OpenApiParameter(name="setAsPrimary", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY),
        OpenApiParameter(name="position", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY),
    ],
    responses={200: ProductResponseDto}
)
@api_view(["POST"])
def product_images(request, productId):
    return Response({
        "id": productId,
        "name": "Design System Pro Kit",
        "price": 99.0,
        "categoryId": "cat_ui",
        "type": "Digital",
        "stockStatus": "InStock",
        "images": ["https://example.com/new_item_img.png"]
    })
