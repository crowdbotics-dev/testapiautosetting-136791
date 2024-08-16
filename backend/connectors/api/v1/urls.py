from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136791ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136791", Testconnectors136791ViewSet, basename="testconnectors136791"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
