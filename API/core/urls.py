from django.urls import path
from core.controllers import (
    health_controller,
    database_controller,
    schema_controller,
    table_controller,
    column_controller,
    row_controller,
    constraint_controller,
)

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

    # Table Management Endpoints
    path("databases/<str:db>/schemas/<str:schema>/tables", table_controller.table_list, name="table_list"),
    path("databases/<str:db>/schemas/<str:schema>/tables/<str:table>", table_controller.table_detail, name="table_detail"),

    # Column Management Endpoints
    path("databases/<str:db>/schemas/<str:schema>/tables/<str:table>/columns", column_controller.column_list, name="column_list"),
    path("databases/<str:db>/schemas/<str:schema>/tables/<str:table>/columns/<str:column>", column_controller.column_detail, name="column_detail"),

    # Row Data Endpoints
    path("databases/<str:db>/schemas/<str:schema>/tables/<str:table>/rows", row_controller.row_list, name="row_list"),
    path("databases/<str:db>/schemas/<str:schema>/tables/<str:table>/rows/<int:id>", row_controller.row_detail, name="row_detail"),

    # Constraint Management Endpoints
    path("constraints/check", constraint_controller.create_check_constraint, name="create_check_constraint"),
    path("constraints/primarykey", constraint_controller.create_primary_key, name="create_primary_key"),
    path("constraints/unique", constraint_controller.create_unique_constraint, name="create_unique_constraint"),
    path("constraints/foreignkey", constraint_controller.create_foreign_key, name="create_foreign_key"),
    path("constraints/<str:constraintId>", constraint_controller.constraint_detail, name="constraint_detail"),
]




