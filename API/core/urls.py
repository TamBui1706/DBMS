from django.urls import path
from core.controllers import health_controller, database_controller, schema_controller

urlpatterns = [
    # Health & Metrics Endpoints
    path("health", health_controller.get_health, name="health"),
    path("metrics", health_controller.get_metrics, name="metrics"),

    # Database Administration Endpoints
    path("databases", database_controller.database_list, name="database_list"),
    path("databases/<str:db>", database_controller.database_detail, name="database_detail"),
    path("databases/<str:db>/open", database_controller.open_database, name="open_database"),
    path("databases/<str:db>/close", database_controller.close_database, name="close_database"),
    path("databases/<str:db>/readonly", database_controller.set_readonly_database, name="set_readonly_database"),
    path("databases/<str:db>/recovery", database_controller.run_database_recovery, name="run_database_recovery"),

    # Schema Management Endpoints
    path("databases/<str:db>/schemas", schema_controller.schema_list, name="schema_list"),
    path("databases/<str:db>/schemas/<str:schema>", schema_controller.schema_detail, name="schema_detail"),
]

