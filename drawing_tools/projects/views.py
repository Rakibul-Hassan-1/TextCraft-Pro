from rest_framework.views import APIView
from rest_framework.response import Response

class ProjectListView(APIView):
    def get(self, request):
        return Response({"message": "Project list endpoint"})

class ProjectDetailView(APIView):
    def get(self, request, pk):
        return Response({"message": f"Details for project {pk}"})
