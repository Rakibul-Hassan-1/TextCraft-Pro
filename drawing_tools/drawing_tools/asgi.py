import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from canvas.consumers import CanvasConsumer
from chat.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drawing_tools.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/canvas/", CanvasConsumer.as_asgi()),
            path("ws/chat/", ChatConsumer.as_asgi()),
        ])
    ),
})
