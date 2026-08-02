from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from AssignmentStore.Services.customer_service import CustomerService
from AssignmentStore.DTOs.customer_dto import CreateCustomerRequestDto, CustomerResponseDto

customer_service = CustomerService()

@extend_schema(
    parameters=[
        OpenApiParameter(name="Search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, description="Search term"),
        OpenApiParameter(name="Status", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, description="Status filter"),
        OpenApiParameter(name="Category", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, description="Category filter"),
        OpenApiParameter(name="CreatedFrom", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY, description="Created from date"),
        OpenApiParameter(name="CreatedTo", type=OpenApiTypes.DATETIME, location=OpenApiParameter.QUERY, description="Created to date"),
        OpenApiParameter(name="Sort", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, description="Sort order"),
        OpenApiParameter(name="Page", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, description="Page number"),
        OpenApiParameter(name="PageSize", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, description="Page size"),
        OpenApiParameter(name="SendInvitation", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY, description="Send invitation flag"),
    ],
    request=CreateCustomerRequestDto,
    responses={200: CustomerResponseDto(many=True), 201: CustomerResponseDto}
)
@api_view(["GET", "POST"])
def customer_list(request):
    if request.method == "GET":
        search = request.query_params.get("Search")
        status_param = request.query_params.get("Status")
        category = request.query_params.get("Category")
        
        data = customer_service.list_customers(search=search, status=status_param, category=category)
        return Response(CustomerResponseDto(data, many=True).data)
        
    elif request.method == "POST":
        serializer = CreateCustomerRequestDto(data=request.data)
        if serializer.is_valid():
            company_name = serializer.validated_data["companyName"]
            domain = serializer.validated_data.get("domain", "")
            status_val = serializer.validated_data.get("status", "Prospect")
            category = serializer.validated_data.get("category", "")
            desc = serializer.validated_data.get("description", "")
            users = serializer.validated_data.get("users", [])
            
            created = customer_service.create_customer(
                company_name=company_name,
                domain=domain,
                status=status_val,
                category=category,
                description=desc,
                users_data=users
            )
            return Response(CustomerResponseDto(created).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(responses={200: CustomerResponseDto})
@api_view(["GET", "DELETE"])
def customer_detail(request, customerId):
    if request.method == "GET":
        data = customer_service.get_customer(customerId)
        if not data:
            return Response({"detail": f"Customer '{customerId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(CustomerResponseDto(data).data)
        
    elif request.method == "DELETE":
        success = customer_service.delete_customer(customerId)
        if not success:
            return Response({"detail": f"Customer '{customerId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Customer '{customerId}' deleted successfully."}, status=status.HTTP_200_OK)

