from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VoiceModelViewSet, generate_speech

router = DefaultRouter()
router.register(r'voices', VoiceModelViewSet)

urlpatterns = [
    path('', include(router.urls)),  # API endpoints for voice models
    path('generate_speech/', generate_speech, name="generate_speech"),  # TTS API
]
