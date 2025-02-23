from rest_framework import viewsets
from .models import Algorithm
from .serializers import AlgorithmSerializer

class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer
