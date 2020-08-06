# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# def index(request):
#     return render(request, 'chatapi/index.html', {})

@login_required(login_url='/api-auth/login/')
def room(request):
    return render(request, 'chatapi/room.html', { })