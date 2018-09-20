"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import settings

def static_url():
    from django.views import static
    urlpattern = url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static')
    return urlpattern

def image_url():
    from django.views import static
    urlpattern = url(r'^media/img/(?P<path>.*)$', static.serve, {'document_root': settings.PICTURE_ROOT}, name='media')
    return urlpattern

urlpatterns = [
    static_url(),
    image_url(),
    url('article/', include('article.urls')),
    url('myplayer/', include('myplayer.urls')),
    url('rtmp/', include('rtmpstreamer.urls')),
]
