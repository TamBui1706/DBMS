# Guide: Generating Swagger UI (OpenAPI 3.0) for Django REST API

To generate an interactive Swagger UI documentation interface (like the one in your screenshot) from our Django project, we will use **`drf-spectacular`**, which is the modern standard OpenAPI 3.0 generator for Django REST Framework.

---

## Step 1: Install `drf-spectacular`
Open your terminal and install the package:
```bash
pip install drf-spectacular
```

---

## Step 2: Configure Django Settings (`API/dbms_api/settings.py`)
Add the package to your `INSTALLED_APPS` and register it as the default schema generator for Django REST Framework.

1.  **Add to `INSTALLED_APPS`**:
    ```python
    INSTALLED_APPS = [
        ...
        "rest_framework",
        "drf_spectacular",  # Add this line
        "core",
    ]
    ```

2.  **Configure REST Framework Schema Class**:
    Add the following configuration to the bottom of the file:
    ```python
    REST_FRAMEWORK = {
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
        "DEFAULT_AUTHENTICATION_CLASSES": [],
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.AllowAny",
        ],
    }

    SPECTACULAR_SETTINGS = {
        "TITLE": "DBMS API",
        "DESCRIPTION": "REST API documentation for the DBMS project.",
        "VERSION": "1.0.0",
        "SERVE_INCLUDE_SCHEMA": False,
    }
    ```

---

## Step 3: Configure URL Routing (`API/dbms_api/urls.py`)
Register the routes to expose the raw schema (JSON/YAML) and render the interactive Swagger UI dashboard.

Modify `API/dbms_api/urls.py` as follows:
```python
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
            "swagger-ui": "/api/schema/swagger-ui/"  # Added reference
        }
    })

urlpatterns = [
    path("", root_view, name="root_view"),
    path("api/v1/", include("core.urls")),
    
    # OpenAPI Schema & Swagger UI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
```

---

## Step 4: Run the Server and View Swagger UI
Start your development server:
```powershell
$env:PYTHONPATH=".;API"
python API/manage.py runserver
```

Now, open your browser and navigate to:
👉 **`http://127.0.0.1:8000/api/schema/swagger-ui/`**

You will see the exact same interactive Swagger UI page as shown in your screenshot, where you can:
*   Expand each endpoint (GET, POST, PUT, DELETE).
*   View request parameter schemas and example values.
*   Click **"Try it out"** to execute real API requests directly from the browser!

---

## Step 5: Export OpenAPI JSON File (`dbms-openapi.json`)
If you need to export the static JSON file (for GitHub Pages deployment like in your screenshot `manaxpow.github.io/DBMS/swagger/`), run this command:

```powershell
$env:PYTHONPATH=".;API"
python API/manage.py spectacular --file dbms-openapi.json --format openapi-json
```
This generates a `dbms-openapi.json` file in your workspace directory containing the full OpenAPI 3.0 specification.

---

## Step 6: Deploying to GitHub Pages
Since GitHub Pages only hosts static files, we render the Swagger interface using a static `index.html` file that loads Swagger UI via CDN.

I have created a `swagger/` folder in your workspace root containing:
*   `swagger/index.html` (the static Swagger UI wrapper).
*   `swagger/dbms-openapi.json` (the API spec copy).

To publish it to your GitHub Pages (`https://TamBui1706.github.io/DBMS/swagger/`):

1.  **Commit and Push the swagger folder to GitHub**:
    ```bash
    git add swagger/
    git commit -m "Add static swagger documentation for github pages"
    git push
    ```

2.  **Enable GitHub Pages**:
    *   Go to your repository page on GitHub: `https://github.com/TamBui1706/DBMS`
    *   Click on **Settings** (tab at the top).
    *   On the left sidebar, click on **Pages** (under the "Code and automation" section).
    *   Under **Build and deployment**, set the source to **Deploy from a branch**.
    *   Under **Branch**, select your branch (e.g., `dev` or `master`) and set the folder to `/ (root)`.
    *   Click **Save**.

After a minute, your interactive Swagger documentation will be live at:
👉 **`https://TamBui1706.github.io/DBMS/swagger/`**


