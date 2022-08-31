import requests
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


@shared_task
def get_active_calls():
    url = 'http://localhost:8000/api/listcalls/?format=json'
    response = requests.get(url)
    async_to_sync(channel_layer.group_send)('active_calls', {'type': 'send_active_calls', 'text': response.json()})
