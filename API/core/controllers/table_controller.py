from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.services.table_service import TableService
from core.dto.request.table_request import CreateTableRequest, UpdateTableRequest
from core.dto.response.table_response import TableResponse

table_service = TableService()

@extend_schema(
    request=CreateTableRequest,
    responses={200: TableResponse(many=True), 201: TableResponse}
)
@api_view(["GET", "POST"])
def table_list(request, db, schema):
    if request.method == "GET":
        data = table_service.list_tables(schema)
        if data is None:
            return Response({"detail": f"Schema '{schema}' not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TableResponse(data, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = CreateTableRequest(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            new_table = table_service.create_table(schema, name)
            if not new_table:
                return Response({"detail": f"Table '{name}' already exists or Schema '{schema}' not found."}, status=status.HTTP_400_BAD_REQUEST)
                
            response_serializer = TableResponse(new_table)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=UpdateTableRequest,
    responses={200: TableResponse}
)
@api_view(["GET", "PUT", "DELETE"])
def table_detail(request, db, schema, table):


    if request.method == "GET":
        data = table_service.get_table(schema, table)
        if not data:
            return Response({"detail": f"Table '{table}' not found in schema '{schema}'."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TableResponse(data)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        serializer = UpdateTableRequest(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            updated = table_service.update_table(schema, table, name)
            if not updated:
                return Response({"detail": f"Table '{table}' not found in schema '{schema}'."}, status=status.HTTP_404_NOT_FOUND)
            response_serializer = TableResponse(updated)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        success = table_service.delete_table(schema, table)
        if not success:
            return Response({"detail": f"Table '{table}' not found in schema '{schema}'."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Table '{table}' deleted successfully."}, status=status.HTTP_200_OK)
