from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CanvasConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "canvas_room"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "canvas_update", "data": data}
        )

    async def canvas_update(self, event):
        await self.send(text_data=json.dumps(event['data']))
