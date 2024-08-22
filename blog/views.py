from django.shortcuts import render
from .models import *

def index(request):
    Posts = Post.objects.all().order_by('publishedDate')
    context = {
        'post':Posts
    }
    return render(request, 'index.html', context)
# Create your views here.
def search_results(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'posts': results, 'query': query})