from django.shortcuts import render, get_object_or_404, redirect
from .models import ChatRoom
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})



@login_required
def index(request):
    user_rooms = request.user.chat_rooms.all()
    return render(request, 'chat/index.html', {'user_rooms': user_rooms})

@login_required
def room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    messages = room.messages.order_by('timestamp')
    context = {'room_name': room_name,
                'messages': messages,
                'room':room,            
            }
    return render(request, 'chat/room.html', context)



@login_required
def rooms(request):
    rooms = ChatRoom.objects.all()
    context = {'rooms':rooms}
    return render(request, 'chat/rooms.html', context)


@login_required
def join(request,id):
    room = get_object_or_404(ChatRoom, id=id)
    user = request.user
    room.participants.add(user)
    room.save()
    return redirect('room',room_name=room.name)


@login_required
def leave(request,id):
    room = get_object_or_404(ChatRoom, id=id)
    user = request.user
    room.participants.remove(user)
    room.save()
    return redirect('room',room_name=room.name)



