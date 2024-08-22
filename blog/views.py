from django.shortcuts import render
from .models import Post
from django.db.models import Q

def index(request):
    posts = Post.objects.all()  
    return render(request, 'index.html', {'posts': posts})

def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        results = Post.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})
def archive_view(request):
    posts = Post.objects.all().order_by('-publishedDate')  # استفاده از فیلد صحیح
    return render(request, 'archive.html', {'posts': posts})

def detail_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post': post})
def AboutView(request):
    return render(request, 'about.html')

def post_titles_view(request):
    titles = Post.objects.all().order_by('-publishedDate')  
    return render(request, 'title.html', {'titles': titles})