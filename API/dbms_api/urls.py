from django.urls import path, include
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({
        "message": "Welcome to the DBMS REST API Gateway",
        "endpoints": {
            "health": "/api/v1/health",
            "metrics": "/api/v1/metrics",
            "databases": "/api/v1/databases"
        }
    })

urlpatterns = [
    path("", root_view, name="root_view"),
    path("api/v1/", include("core.urls")),
]

