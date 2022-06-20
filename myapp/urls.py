from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r"product", ProductViewSet)
urlpatterns = [
    path("", include(router.urls)),
]