from django.shortcuts import render
from .models import *

def index(request):
    Posts = Post.objects.all().order_by('publishedDate')
    context ={
        'post':Posts
    }
    return render(request, 'index.html', context)
# Create your views here.
