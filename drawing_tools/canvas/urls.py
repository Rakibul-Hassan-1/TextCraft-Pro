from django.urls import path
from . import views

urlpatterns = [
    path('draw/', views.CanvasView.as_view(), name='canvas-draw'),
    # Add more canvas-specific URLs here
]
