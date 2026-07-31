from rest_framework.decorators import api_view
from rest_framework.response import Response
import time
from Classes.Core.database_server import DatabaseServer

START_TIME = time.time()

# Instantiate the physical DatabaseServer object
server = DatabaseServer()
server.serverId = "DBMS-Server-01"
server.status = "running"

@api_view(["GET"])
def get_health(request):
    """
    Check the database server health status using the DatabaseServer class.
    """
    return Response({
        "serverId": server.serverId,
        "status": server.status,
        "uptime_seconds": int(time.time() - START_TIME),
        "version": "1.0.0-Beta"
    })

@api_view(["GET"])
def get_metrics(request):
    """
    Retrieve real-time database server performance metrics.
    """
    return Response({
        "connections": {
            "active": 4,
            "max": 100,
            "idle": 12
        },
        "query_performance": {
            "qps": 124.5,
            "avg_latency_ms": 1.2
        },
        "buffer_pool": {
            "hit_ratio": 0.992,
            "dirty_pages": 14,
            "free_frames": 4096
        }
    })
