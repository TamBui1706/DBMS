from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.services.row_service import RowService
from core.dto.request.row_request import InsertRowRequest, UpdateRowRequest
from core.dto.response.row_response import RowResponse

row_service = RowService()

@extend_schema(
    request=InsertRowRequest,
    responses={200: RowResponse(many=True), 201: RowResponse}
)
@api_view(["GET", "POST"])
def row_list(request, db, schema, table):
    if request.method == "GET":
        data = row_service.list_rows(table)
        if data is None:
            return Response({"detail": f"Table '{table}' not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RowResponse(data, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = InsertRowRequest(data=request.data)
        if serializer.is_valid():
            values = serializer.validated_data["values"]
            new_row = row_service.insert_row(table, values)
            if not new_row:
                return Response({"detail": f"Table '{table}' not found."}, status=status.HTTP_400_BAD_REQUEST)
                
            response_serializer = RowResponse(new_row)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=UpdateRowRequest,
    responses={200: RowResponse}
)
@api_view(["GET", "PUT", "DELETE"])
def row_detail(request, db, schema, table, id):


    if request.method == "GET":
        data = row_service.get_row(table, id)
        if not data:
            return Response({"detail": f"Row '{id}' not found in table '{table}'."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RowResponse(data)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        serializer = UpdateRowRequest(data=request.data)
        if serializer.is_valid():
            values = serializer.validated_data["values"]
            updated = row_service.update_row(table, id, values)
            if not updated:
                return Response({"detail": f"Row '{id}' not found in table '{table}'."}, status=status.HTTP_404_NOT_FOUND)
            response_serializer = RowResponse(updated)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        success = row_service.delete_row(table, id)
        if not success:
            return Response({"detail": f"Row '{id}' not found in table '{table}'."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Row '{id}' deleted successfully."}, status=status.HTTP_200_OK)
