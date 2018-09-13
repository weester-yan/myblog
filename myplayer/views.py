from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myplayer.models import Myplayer
from datetime import datetime

def player(request):
    post_list = Myplayer.objects.all()
    return render(request, 'myplayer/player.html', {'post_list' : post_list})
