from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.services.column_service import ColumnService
from core.dto.request.column_request import AddColumnRequest, UpdateColumnRequest
from core.dto.response.column_response import ColumnResponse

column_service = ColumnService()

@api_view(["GET", "POST"])
def column_list(request, table):
    if request.method == "GET":
        data = column_service.list_columns(table)
        if data is None:
            return Response({"detail": f"Table '{table}' not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ColumnResponse(data, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = AddColumnRequest(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            col_type = serializer.validated_data["type"]
            new_col = column_service.add_column(table, name, col_type)
            if not new_col:
                return Response({"detail": f"Column '{name}' already exists or Table '{table}' not found."}, status=status.HTTP_400_BAD_REQUEST)
                
            response_serializer = ColumnResponse(new_col)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT", "DELETE"])
def column_detail(request, table, column):
    if request.method == "PUT":
        serializer = UpdateColumnRequest(data=request.data)
        if serializer.is_valid():
            col_type = serializer.validated_data["type"]
            updated = column_service.update_column(table, column, col_type)
            if not updated:
                return Response({"detail": f"Column '{column}' not found in table '{table}'."}, status=status.HTTP_404_NOT_FOUND)
            response_serializer = ColumnResponse(updated)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        success = column_service.delete_column(table, column)
        if not success:
            return Response({"detail": f"Column '{column}' not found in table '{table}'."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Column '{column}' deleted successfully."}, status=status.HTTP_200_OK)
