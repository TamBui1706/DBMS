from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.services.database_service import DatabaseService
from core.dto.request.database_request import CreateDatabaseRequest
from core.dto.response.database_response import DatabaseResponse

db_service = DatabaseService()

@api_view(["GET", "POST"])
def database_list(request):
    if request.method == "GET":
        data = db_service.list_databases()
        serializer = DatabaseResponse(data, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = CreateDatabaseRequest(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            owner = serializer.validated_data.get("owner", "admin")
            description = serializer.validated_data.get("description", "")
            
            new_db = db_service.create_database(name, owner, description)
            if not new_db:
                return Response({"detail": f"Database '{name}' already exists."}, status=status.HTTP_400_BAD_REQUEST)
                
            response_serializer = DatabaseResponse(new_db)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "DELETE"])
def database_detail(request, db):
    if request.method == "GET":
        data = db_service.get_database(db)
        if not data:
            return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = DatabaseResponse(data)
        return Response(serializer.data)
        
    elif request.method == "DELETE":
        success = db_service.delete_database(db)
        if not success:
            return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": f"Database '{db}' deleted successfully."}, status=status.HTTP_200_OK)

@api_view(["POST"])
def open_database(request, db):
    data = db_service.open_database(db)
    if not data:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = DatabaseResponse(data)
    return Response(serializer.data)

@api_view(["POST"])
def close_database(request, db):
    data = db_service.close_database(db)
    if not data:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = DatabaseResponse(data)
    return Response(serializer.data)

@api_view(["POST"])
def set_readonly_database(request, db):
    data = db_service.set_readonly_database(db)
    if not data:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = DatabaseResponse(data)
    return Response(serializer.data)

@api_view(["POST"])
def run_database_recovery(request, db):
    data = db_service.run_database_recovery(db)
    if not data:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = DatabaseResponse(data)
    return Response(serializer.data)
