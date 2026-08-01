from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.services.schema_service import SchemaService
from core.dto.request.schema_request import CreateSchemaRequest, UpdateSchemaRequest
from core.dto.response.schema_response import SchemaResponse

schema_service = SchemaService()

@extend_schema(
    request=CreateSchemaRequest,
    responses={200: SchemaResponse(many=True), 201: SchemaResponse}
)
@api_view(["GET", "POST"])
def schema_list(request, db):
    if request.method == "GET":
        data = schema_service.list_schemas(db)
        if data is None:
            return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SchemaResponse(data, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = CreateSchemaRequest(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            new_schema = schema_service.create_schema(db, name)
            if not new_schema:
                return Response({"detail": f"Schema '{name}' already exists or Database '{db}' not found."}, status=status.HTTP_400_BAD_REQUEST)
                
            response_serializer = SchemaResponse(new_schema)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=UpdateSchemaRequest,
    responses={200: SchemaResponse}
)
@api_view(["GET", "PUT", "DELETE"])
def schema_detail(request, db, schema):

    if request.method == "GET":
        data = schema_service.get_schema(db, schema)
        if not data:
            return Response({"detail": f"Schema '{schema}' not found in database '{db}'."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SchemaResponse(data)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        serializer = UpdateSchemaRequest(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            updated = schema_service.update_schema(db, schema, name)
            if not updated:
                return Response({"detail": f"Schema '{schema}' not found in database '{db}'."}, status=status.HTTP_404_NOT_FOUND)
            response_serializer = SchemaResponse(updated)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        success = schema_service.delete_schema(db, schema)
        if not success:
            return Response({"detail": f"Schema '{schema}' not found in database '{db}'."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Schema '{schema}' deleted successfully."}, status=status.HTTP_200_OK)
