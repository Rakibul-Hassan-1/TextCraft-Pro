from rest_framework import viewsets
from .serializers import GeeksSerializer
from .models import GeeksModel

class GeeksViewSet(viewsets.ModelViewSet):
	queryset = GeeksModel.objects.all()
	serializer_class = GeeksSerializer
