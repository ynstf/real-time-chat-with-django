from django.shortcuts import render, get_object_or_404, redirect
from .models import ChatRoom
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
                'room':room}
    return render(request, 'chat/room.html', context)




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


