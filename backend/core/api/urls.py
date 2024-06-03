from rest_framework.routers import DefaultRouter
from django.urls import path, include
from customers.api.urls import customer_router

router = DefaultRouter()

# app1
# app2
# customers App
router.registry.extend(customer_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]