from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rtmpstreamer.models import Rtmpstr
from datetime import datetime

def rtmpstr(request):
    post_list = Rtmpstr.objects.all()
    return render(request, 'rtmpstreamer/index.html', {'post_list' : post_list})
