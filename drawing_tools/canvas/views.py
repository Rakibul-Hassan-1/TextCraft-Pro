from rest_framework.views import APIView
from rest_framework.response import Response

class CanvasView(APIView):
    def get(self, request):
        return Response({"message": "Canvas endpoint"})
