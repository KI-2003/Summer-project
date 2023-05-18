from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Room

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def enter_room(request):
    
    if request.method == 'POST':
        room_name = request.POST['room_name']
        password = request.POST['password']

        try:
            room = Room.objects.get(name=room_name, password=password)
        except Room.DoesNotExist:
            error_message = 'Invalid room name or password.'
            return render(request,'room/rooms.html',{'error_message':error_message})

        # Perform actions after successful room entry
        # For example, you could redirect the user to a success page or perform additional logic here.

        messages = Message.objects.filter(room=room)[0:25]
        return render(request, 'room/room.html',{'room': room, 'messages': messages})
    
    return render(request, 'room/rooms.html')
