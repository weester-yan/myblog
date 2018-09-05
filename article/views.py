from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

def home(request):
    post_list = Article.objects.all()
    return render(request, 'article/home.html', {'post_list' : post_list})
