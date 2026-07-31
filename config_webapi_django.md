# Guide: Configuring the DBMS Web API using Django REST Framework

This document provides a comprehensive step-by-step guide on how the Web API for the DBMS is configured, structured, and executed using **Django** and **Django REST Framework (DRF)**.

---

## 1. Prerequisites and Installation
To run the Web API, the required dependencies must be installed in your Python environment:

```bash
pip install django djangorestframework
```

---

## 2. Django Configuration Directory Structure
The API is cleanly isolated inside the `API/` directory at the project root:

```
API/
├── manage.py               # Django CLI management entrypoint
├── dbms_api/               # Project configuration package
│   ├── __init__.py
│   ├── settings.py         # Global settings (CORS, DRF config, DATABASES)
│   ├── urls.py             # Root URL routing (redirects to api/v1/)
│   └── wsgi.py
└── core/                   # Subsystem Application
    ├── __init__.py
    ├── apps.py
    ├── serializers.py      # Request/Response validation serializers
    ├── urls.py             # Endpoint routing matching the Mindmap
    └── views/              # Modular controller package
        ├── __init__.py
        ├── health.py       # Health & Metrics handlers
        └── database.py     # Database CRUD & operations handlers
```

---

## 3. Project Configuration Setup

### A. Django Settings (`API/dbms_api/settings.py`)
The project utilizes a minimal, lightweight setup suitable for local development:
*   **Installed Apps**: Registered `rest_framework` and `core`.
*   **Databases**: Uses an in-memory SQLite database (`:memory:`) to ensure no persistent files are created by Django itself, keeping the DBMS engine clean.
*   **Authentication & Permissions**: Open access configured in `REST_FRAMEWORK` settings:

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}
```

### B. App URL Dispatcher (`API/core/urls.py`)
Routes HTTP requests to their respective split view handlers:

```python
from django.urls import path
from core.views import health, database

urlpatterns = [
    # Health & Telemetry
    path("health", health.get_health, name="health"),
    path("metrics", health.get_metrics, name="metrics"),

    # Database Resource Managers
    path("databases", database.database_list, name="database_list"),
    path("databases/<str:db>", database.database_detail, name="database_detail"),
    
    # Database Actions
    path("databases/<str:db>/open", database.open_database, name="open_database"),
    path("databases/<str:db>/close", database.close_database, name="close_database"),
    path("databases/<str:db>/readonly", database.set_readonly_database, name="set_readonly_database"),
    path("databases/<str:db>/recovery", database.run_database_recovery, name="run_database_recovery"),
]
```

---

## 4. Business Logic Integration (Views)
Rather than using static mock data, the views dynamically import and instantiate the core classes of the DBMS located in the `Classes/` directory:

```python
# API/core/views/database.py imports actual project classes:
from Classes.Core.database import Database
from Classes.DatabaseObjectManagement.schema import Schema
```

*   **Composite Pattern Assembly**: When creating a database via `POST /databases`, a real `Database` object is created and a default `Schema("public")` component is attached to it recursively.
*   **Telemetric Binding**: The `health` views instantiate the actual `DatabaseServer` instance and check its real attributes (`serverId`, `status`).

---

## 5. Execution and Testing

### Start the Server
Run the dev server from the project root by setting the python path to include both the root and `API/` directory:

```powershell
$env:PYTHONPATH=".;API"
python API/manage.py runserver 127.0.0.1:8000
```

### Verification Endpoints
| HTTP Verb | Endpoint | Action |
| :--- | :--- | :--- |
| **GET** | `/api/v1/health` | Check DBMS server availability status |
| **GET** | `/api/v1/metrics` | Retrieve memory/buffer pool hit telemetry |
| **GET** | `/api/v1/databases` | List metadata of active database objects |
| **POST** | `/api/v1/databases` | Initialize a new Database object |
| **POST** | `/api/v1/databases/{db}/open` | Trigger the physical connection open method |
| **POST** | `/api/v1/databases/{db}/recovery` | Replay the WAL index recovery logs |
