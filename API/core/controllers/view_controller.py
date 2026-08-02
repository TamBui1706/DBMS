from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.services.view_service import ViewService
from core.dto.request.view_request import CreateViewRequest, UpdateViewRequest
from core.dto.response.view_response import ViewResponse

view_service = ViewService()

@extend_schema(request=CreateViewRequest, responses={201: ViewResponse, 200: ViewResponse(many=True)})
@api_view(["GET", "POST"])
def view_list(request):
    if request.method == "GET":
        data = view_service.list_views()
        serializer = ViewResponse(data, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = CreateViewRequest(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            query_definition = serializer.validated_data["query_definition"]
            # Let's default to public schema for view creation
            new_v = view_service.create_view("public", name, query_definition)
            if not new_v:
                return Response({"detail": f"View '{name}' already exists or schema not found."}, status=status.HTTP_400_BAD_REQUEST)
            return Response(ViewResponse(new_v).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=UpdateViewRequest, responses={200: ViewResponse})
@api_view(["GET", "PUT", "DELETE"])
def view_detail(request, viewName):
    if request.method == "GET":
        data = view_service.get_view(viewName)
        if not data:
            return Response({"detail": f"View '{viewName}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(ViewResponse(data).data)
        
    elif request.method == "PUT":
        serializer = UpdateViewRequest(data=request.data)
        if serializer.is_valid():
            query_definition = serializer.validated_data["query_definition"]
            updated = view_service.update_view(viewName, query_definition)
            if not updated:
                return Response({"detail": f"View '{viewName}' not found."}, status=status.HTTP_404_NOT_FOUND)
            return Response(ViewResponse(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        success = view_service.delete_view(viewName)
        if not success:
            return Response({"detail": f"View '{viewName}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"View '{viewName}' deleted successfully."}, status=status.HTTP_200_OK)
