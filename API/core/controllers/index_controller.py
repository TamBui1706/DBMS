from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.services.index_service import IndexService
from core.dto.request.index_request import CreateIndexRequest, IndexSearchRequest, IndexRangeSearchRequest
from core.dto.response.index_response import IndexResponse, IndexSearchResponse

index_service = IndexService()

@extend_schema(request=CreateIndexRequest, responses={201: IndexResponse, 200: IndexResponse(many=True)})
@api_view(["GET", "POST"])
def index_list(request, db, schema, table):
    if request.method == "GET":
        data = index_service.list_indexes(table)
        if data is None:
            return Response({"detail": f"Table '{table}' not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = IndexResponse(data, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = CreateIndexRequest(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            idx_type = serializer.validated_data["type"]
            col_name = serializer.validated_data["column_name"]
            
            new_idx = index_service.create_index(table, name, idx_type, col_name)
            if not new_idx:
                return Response({"detail": f"Index creation failed. Table '{table}' not found or type invalid."}, status=status.HTTP_400_BAD_REQUEST)
                
            response_serializer = IndexResponse(new_idx)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(responses={200: None})
@api_view(["DELETE"])
def index_detail(request, db, schema, table, index):
    success = index_service.delete_index(table, index)
    if not success:
        return Response({"detail": f"Index '{index}' not found in table '{table}'."}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message": f"Index '{index}' deleted successfully."}, status=status.HTTP_200_OK)

@extend_schema(request=IndexSearchRequest, responses={200: IndexSearchResponse})
@api_view(["POST"])
def index_search(request, db, schema, table, index):
    serializer = IndexSearchRequest(data=request.data)
    if serializer.is_valid():
        key = serializer.validated_data["key"]
        results = index_service.search_index(table, index, key)
        if not results:
            return Response({"detail": f"Index '{index}' not found in table '{table}'."}, status=status.HTTP_404_NOT_FOUND)
        return Response(IndexSearchResponse(results).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=IndexRangeSearchRequest, responses={200: IndexSearchResponse})
@api_view(["POST"])
def index_range_search(request, db, schema, table, index):
    serializer = IndexRangeSearchRequest(data=request.data)
    if serializer.is_valid():
        start_key = serializer.validated_data["start_key"]
        end_key = serializer.validated_data["end_key"]
        results = index_service.range_search_index(table, index, start_key, end_key)
        if not results:
            return Response({"detail": f"Index '{index}' not found in table '{table}'."}, status=status.HTTP_404_NOT_FOUND)
        return Response(IndexSearchResponse(results).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
