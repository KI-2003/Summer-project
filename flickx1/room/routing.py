from django.urls import path
from . import consumers

websocket_urlpatterns = [
	url(r'^ws/room/(?P<room_name>[^/]+)/$',consumers.ChatConsumer.as_asgi()),
	
]
