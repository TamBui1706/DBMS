from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Import project's actual object management classes
from Classes.Core.database import Database
from Classes.DatabaseObjectManagement.schema import Schema

# Global registry storing instances of Database classes
ACTIVE_DATABASES = {}

# Seed initial Database objects to demonstrate DBMS Object hierarchy
db_production = Database(name="ProductionDB")
db_production.status = "open"
db_production.owner = "admin"
db_production.size_mb = 170.0
db_production.add_child(Schema(name="public"))
db_production.add_child(Schema(name="sales"))
db_production.add_child(Schema(name="inventory"))
ACTIVE_DATABASES["ProductionDB"] = db_production

db_test = Database(name="TestDB")
db_test.status = "closed"
db_test.owner = "developer"
db_test.size_mb = 12.5
db_test.add_child(Schema(name="public"))
ACTIVE_DATABASES["TestDB"] = db_test

def get_database_api_response(db: Database) -> dict:
    """
    Helper to extract metadata from the Database composite node
    and attach API-specific fields.
    """
    metadata = db.get_metadata()
    schemas = [child["name"] for child in metadata.get("children", []) if child.get("type") == "Schema"]
    
    return {
        "name": db.name,
        "owner": getattr(db, "owner", "admin"),
        "status": getattr(db, "status", "closed"),
        "size_mb": getattr(db, "size_mb", 0.0),
        "description": getattr(db, "description", ""),
        "schemas": schemas
    }

@api_view(["GET", "POST"])
def database_list(request):
    """
    List databases or create a new database.
    """
    if request.method == "GET":
        serialized_dbs = [get_database_api_response(db) for db in ACTIVE_DATABASES.values()]
        return Response(serialized_dbs)
        
    elif request.method == "POST":
        name = request.data.get("name")
        if not name:
            return Response({"detail": "Database name is required."}, status=status.HTTP_400_BAD_REQUEST)
            
        if name in ACTIVE_DATABASES:
            return Response({"detail": f"Database '{name}' already exists."}, status=status.HTTP_400_BAD_REQUEST)
            
        # Instantiate a real Database class object
        new_db = Database(name=name)
        new_db.owner = request.data.get("owner", "admin")
        new_db.status = "closed"
        new_db.size_mb = 0.0
        new_db.description = request.data.get("description", "")
        new_db.add_child(Schema(name="public"))
        
        ACTIVE_DATABASES[name] = new_db
        return Response(get_database_api_response(new_db), status=status.HTTP_201_CREATED)

@api_view(["GET", "DELETE"])
def database_detail(request, db):
    """
    Get or delete a specific database.
    """
    if db not in ACTIVE_DATABASES:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        return Response(get_database_api_response(ACTIVE_DATABASES[db]))
        
    elif request.method == "DELETE":
        del ACTIVE_DATABASES[db]
        return Response({"message": f"Database '{db}' deleted successfully."}, status=status.HTTP_200_OK)

@api_view(["POST"])
def open_database(request, db):
    if db not in ACTIVE_DATABASES:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
    
    # Call the actual open() method on the Database object
    ACTIVE_DATABASES[db].open()
    ACTIVE_DATABASES[db].status = "open"
    return Response(get_database_api_response(ACTIVE_DATABASES[db]))

@api_view(["POST"])
def close_database(request, db):
    if db not in ACTIVE_DATABASES:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
    
    ACTIVE_DATABASES[db].status = "closed"
    return Response(get_database_api_response(ACTIVE_DATABASES[db]))

@api_view(["POST"])
def set_readonly_database(request, db):
    if db not in ACTIVE_DATABASES:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
    
    ACTIVE_DATABASES[db].status = "readonly"
    return Response(get_database_api_response(ACTIVE_DATABASES[db]))

@api_view(["POST"])
def run_database_recovery(request, db):
    if db not in ACTIVE_DATABASES:
        return Response({"detail": f"Database '{db}' not found."}, status=status.HTTP_404_NOT_FOUND)
    
    ACTIVE_DATABASES[db].status = "closed"
    return Response(get_database_api_response(ACTIVE_DATABASES[db]))
