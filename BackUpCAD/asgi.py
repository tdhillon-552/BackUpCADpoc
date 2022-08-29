import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from BackUpDispatch.routing import ws_urlpatters

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BackUpCAD.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatters))
})
