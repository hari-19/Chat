
# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/api-auth/login/')
def room(request):
    return render(request, 'chat/room.html')