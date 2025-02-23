from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlgorithmViewSet

router = DefaultRouter()
router.register(r'algorithms', AlgorithmViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
