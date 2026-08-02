from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.services.partition_service import PartitionService
from core.dto.request.partition_request import CreatePartitionRequest, UpdatePartitionRequest
from core.dto.response.partition_response import PartitionResponse

partition_service = PartitionService()

@extend_schema(request=CreatePartitionRequest, responses={201: PartitionResponse, 200: PartitionResponse(many=True)})
@api_view(["GET", "POST"])
def partition_list(request):
    if request.method == "GET":
        table_name = request.query_params.get("tableName")
        data = partition_service.list_partitions(table_name)
        serializer = PartitionResponse(data, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = CreatePartitionRequest(data=request.data)
        if serializer.is_valid():
            table_name = serializer.validated_data["table_name"]
            partition_key = serializer.validated_data["partition_key"]
            
            new_p = partition_service.create_partition(table_name, partition_key)
            if not new_p:
                return Response({"detail": f"Table '{table_name}' not found."}, status=status.HTTP_400_BAD_REQUEST)
            return Response(PartitionResponse(new_p).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=UpdatePartitionRequest, responses={200: PartitionResponse})
@api_view(["GET", "PUT", "DELETE"])
def partition_detail(request, partitionId):
    if request.method == "GET":
        data = partition_service.get_partition(partitionId)
        if not data:
            return Response({"detail": f"Partition '{partitionId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(PartitionResponse(data).data)
        
    elif request.method == "PUT":
        serializer = UpdatePartitionRequest(data=request.data)
        if serializer.is_valid():
            partition_key = serializer.validated_data["partition_key"]
            updated = partition_service.update_partition(partitionId, partition_key)
            if not updated:
                return Response({"detail": f"Partition '{partitionId}' not found."}, status=status.HTTP_404_NOT_FOUND)
            return Response(PartitionResponse(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        success = partition_service.delete_partition(partitionId)
        if not success:
            return Response({"detail": f"Partition '{partitionId}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Partition '{partitionId}' deleted successfully."}, status=status.HTTP_200_OK)
