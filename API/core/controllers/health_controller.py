from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.services.health_service import HealthService

health_service = HealthService()

@api_view(["GET"])
def get_health(request):
    data = health_service.check_health()
    return Response(data)

@api_view(["GET"])
def get_metrics(request):
    return Response({
        "connections": {"active": 4, "max": 100, "idle": 12},
        "query_performance": {"qps": 124.5, "avg_latency_ms": 1.2},
        "buffer_pool": {"hit_ratio": 0.992, "dirty_pages": 14, "free_frames": 4096}
    })
