from django.urls import path

from . import views
from room.views import enter_room

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('enter-room/', enter_room, name='enter-room'),
]
