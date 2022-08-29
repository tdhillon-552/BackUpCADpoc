#web socket routing file


from django.urls import path
from .consumers import ActiveCallsConsumer

ws_urlpatters = [
    path('ws/activecalls', ActiveCallsConsumer.as_asgi())
]
