from django.urls import path
from AssignmentStore.Controllers import (
    auth_controller,
    overview_controller,
    store_controller,
    product_controller,
    order_controller,
    customer_controller,
    discount_controller,
    subscription_controller,
)

urlpatterns = [
    # 1. Authentication Endpoints
    path("api/v1/auth/login", auth_controller.login, name="store_auth_login"),
    path("api/v1/auth/register", auth_controller.register, name="store_auth_register"),
    path("api/v1/auth/logout", auth_controller.logout, name="store_auth_logout"),
    path("api/v1/auth/refresh-token", auth_controller.refresh_token, name="store_auth_refresh_token"),
    path("api/v1/users/me", auth_controller.user_me, name="store_user_me"),

    # 2. Overview Endpoints
    path("api/v1/overview/summary", overview_controller.overview_summary, name="store_overview_summary"),

    # 3. Store Configuration Endpoints
    path("api/v1/store", store_controller.store_detail, name="store_detail"),
    path("api/v1/store/logo", store_controller.store_logo, name="store_logo"),

    # 4. Product Catalog Endpoints
    path("api/v1/products", product_controller.product_list, name="store_product_list"),
    path("api/v1/products/<str:productId>", product_controller.product_detail, name="store_product_detail"),
    path("api/v1/products/<str:productId>/images", product_controller.product_images, name="store_product_images"),

    # 5. Order Management Endpoints
    path("api/v1/orders", order_controller.order_list, name="store_order_list"),
    path("api/v1/orders/<str:orderId>", order_controller.order_detail, name="store_order_detail"),
    path("api/v1/orders/<str:orderId>/status", order_controller.order_status, name="store_order_status"),

    # 6. Customer & Membership Endpoints
    path("api/v1/customers", customer_controller.customer_list, name="store_customer_list"),
    path("api/v1/customers/<str:customerId>", customer_controller.customer_detail, name="store_customer_detail"),

    # 7. Discount & Promotion Endpoints
    path("api/v1/discounts", discount_controller.discount_list, name="store_discount_list"),

    # 8. Subscription Endpoints
    path("api/v1/subscriptions", subscription_controller.subscription_list, name="store_subscription_list"),
    path("api/v1/subscriptions/<str:subscriptionId>", subscription_controller.subscription_detail, name="store_subscription_detail"),
]
