from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def root_view(request):
    return JsonResponse({
        "message": "Welcome to the DBMS REST API Gateway",
        "endpoints": {
            "health": "/api/v1/health",
            "metrics": "/api/v1/metrics",
            "databases": "/api/v1/databases",
            "swagger-ui": "/api/schema/swagger-ui/"
        }
    })

urlpatterns = [
    path("", root_view, name="root_view"),
    path("api/v1/", include("core.urls")),
    path("", include("AssignmentStore.urls")),
    
    # OpenAPI Schema & Swagger UI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]



