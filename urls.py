from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoreInfoViewSet

router = DefaultRouter()
router.register(r'storeinfo', StoreInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]