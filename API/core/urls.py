from django.urls import path
from core.views import health, database

urlpatterns = [
    # Health & Metrics Endpoints
    path("health", health.get_health, name="health"),
    path("metrics", health.get_metrics, name="metrics"),

    # Database Administration Endpoints
    path("databases", database.database_list, name="database_list"),
    path("databases/<str:db>", database.database_detail, name="database_detail"),
    path("databases/<str:db>/open", database.open_database, name="open_database"),
    path("databases/<str:db>/close", database.close_database, name="close_database"),
    path("databases/<str:db>/readonly", database.set_readonly_database, name="set_readonly_database"),
    path("databases/<str:db>/recovery", database.run_database_recovery, name="run_database_recovery"),
]
