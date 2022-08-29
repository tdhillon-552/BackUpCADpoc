from channels.generic.websocket import AsyncWebsocketConsumer


class ActiveCallsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('active_calls', self.channel_name)
        await self.accept()
        print('connected')

    async def disconnect(self, code):
        await self.channel_layer.group_discard('active_calls', self.channel_name)
        print('disconnected')

    async def send_active_calls(self, event):
        text_message = event['text']

        await self.send(text_message)

