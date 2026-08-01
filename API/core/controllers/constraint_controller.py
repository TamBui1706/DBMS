from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.services.constraint_service import ConstraintService
from core.dto.request.constraint_request import (
    CheckConstraintRequest,
    PrimaryKeyRequest,
    UniqueConstraintRequest,
    ForeignKeyRequest,
    UpdateConstraintRequest,
)
from core.dto.response.constraint_response import ConstraintResponse

constraint_service = ConstraintService()

@extend_schema(request=CheckConstraintRequest, responses={201: ConstraintResponse})
@api_view(["POST"])
def create_check_constraint(request):
    serializer = CheckConstraintRequest(data=request.data)
    if serializer.is_valid():
        table_name = serializer.validated_data["table_name"]
        column_name = serializer.validated_data["column_name"]
        rule = serializer.validated_data["rule"]
        expression = serializer.validated_data["expression"]
        
        data = constraint_service.create_check(table_name, column_name, rule, expression)
        if not data:
            return Response({"detail": f"Table '{table_name}' not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(ConstraintResponse(data).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=PrimaryKeyRequest, responses={201: ConstraintResponse})
@api_view(["POST"])
def create_primary_key(request):
    serializer = PrimaryKeyRequest(data=request.data)
    if serializer.is_valid():
        table_name = serializer.validated_data["table_name"]
        column_name = serializer.validated_data["column_name"]
        rule = serializer.validated_data["rule"]
        
        data = constraint_service.create_primary_key(table_name, column_name, rule)
        if not data:
            return Response({"detail": f"Table '{table_name}' not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(ConstraintResponse(data).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=UniqueConstraintRequest, responses={201: ConstraintResponse})
@api_view(["POST"])
def create_unique_constraint(request):
    serializer = UniqueConstraintRequest(data=request.data)
    if serializer.is_valid():
        table_name = serializer.validated_data["table_name"]
        column_name = serializer.validated_data["column_name"]
        rule = serializer.validated_data["rule"]
        
        data = constraint_service.create_unique(table_name, column_name, rule)
        if not data:
            return Response({"detail": f"Table '{table_name}' not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(ConstraintResponse(data).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=ForeignKeyRequest, responses={201: ConstraintResponse})
@api_view(["POST"])
def create_foreign_key(request):
    serializer = ForeignKeyRequest(data=request.data)
    if serializer.is_valid():
        table_name = serializer.validated_data["table_name"]
        column_name = serializer.validated_data["column_name"]
        rule = serializer.validated_data["rule"]
        ref_table = serializer.validated_data["referenced_table"]
        ref_column = serializer.validated_data["referenced_column"]
        
        data = constraint_service.create_foreign_key(table_name, column_name, rule, ref_table, ref_column)
        if not data:
            return Response({"detail": f"Table '{table_name}' not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(ConstraintResponse(data).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=UpdateConstraintRequest, responses={200: ConstraintResponse})
@api_view(["PUT", "DELETE"])
def constraint_detail(request, constraintId):
    if request.method == "PUT":
        serializer = UpdateConstraintRequest(data=request.data)
        if serializer.is_valid():
            rule = serializer.validated_data["rule"]
            updated = constraint_service.update_constraint(constraintId, rule)
            if not updated:
                return Response({"detail": f"Constraint '{constraintId}' not found."}, status=status.HTTP_404_NOT_FOUND)
            return Response(ConstraintResponse(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        success = constraint_service.delete_constraint(constraintId)
        if not success:
            return Response({"detail": f"Constraint '{constraintId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Constraint '{constraintId}' deleted successfully."}, status=status.HTTP_200_OK)
