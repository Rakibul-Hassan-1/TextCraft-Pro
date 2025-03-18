from rest_framework.views import APIView
from rest_framework.response import Response

class ChatMessagesView(APIView):
    def get(self, request):
        return Response({"message": "Chat messages endpoint"})
