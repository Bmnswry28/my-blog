from django.shortcuts import render, get_object_or_404
from .models import Post, Profile
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.generic import ListView, DetailView

def index(request):
    posts = Post.objects.all()  
    return render(request, 'index.html', {'posts': posts})

from django.shortcuts import render
from .models import Post

def search_results(request):
    query = request.GET.get('q', '')
    if query:
        results = Post.objects.filter(title__icontains=query) | Post.objects.filter(Content__icontains=query)
    else:
        results = Post.objects.none()
    
    return render(request, 'search_results.html', {'results': results, 'query': query})


def archive_view(request):
    posts = Post.objects.all().order_by('-publishedDate')
    return render(request, 'archive.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'page.html', {'post': post})

def AboutView(request):
    return render(request, 'about.html')

def post_titles_view(request):
    titles = Post.objects.all().order_by('-publishedDate')
    return render(request, 'title.html', {'titles': titles})

class ProfileListView(ListView):
    model = Profile
    template_name = 'profile_list.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'
