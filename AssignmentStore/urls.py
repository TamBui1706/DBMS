from django.urls import path
from AssignmentStore.Controllers import customer_controller

urlpatterns = [
    # Customer API Endpoints matching Swagger UI
    path("api/v1/customers", customer_controller.customer_list, name="store_customer_list"),
    path("api/v1/customers/<str:customerId>", customer_controller.customer_detail, name="store_customer_detail"),
]
