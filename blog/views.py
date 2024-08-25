from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Profile,Comment,Category,SocialLink
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
def index(request):
    social_links = SocialLink.objects.all()
    posts = Post.objects.filter(status='published')
    context = {
        'social_links': social_links,
        'posts': posts
    }
    return render(request, 'index.html', context)

def search_results(request):
    query = request.GET.get('q', '')
    if query:
        results = Post.objects.filter(title__icontains=query) | Post.objects.filter(Content__icontains=query)
    else:
        results = Post.objects.none()
    
    return render(request, 'search_results.html', {'results': results, 'query': query})


def category_list(request):
    categories = Category.objects.all()
    social_links = SocialLink.objects.all()
    context = {
        'categories': categories,
       'social_links': social_links
    }
    return render(request, 'archive.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'page.html', {'post': post})

def AboutView(request):
    social_links = SocialLink.objects.all()
    return render(request, 'about.html',{'social_links': social_links})

def post_titles_view(request):
    titles = Post.objects.all().order_by('-publishedDate')
    return render(request, 'title.html', {'titles': titles})

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('home')  # Redirect to home page if not a superuser

class ProfileListView(SuperuserRequiredMixin, ListView):
    model = Profile
    template_name = 'profile_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.filter(user__is_superuser=True)

class ProfileDetailView(SuperuserRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return Profile.objects.filter(user__is_superuser=True)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(is_published=True, parent__isnull=True)
    social_links = SocialLink.objects.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            parent_id = request.POST.get('parent_id')
            parent_comment = None
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id, is_published=True)
                except Comment.DoesNotExist:
                    parent_comment = None
            
            comment = form.save(commit=False)
            comment.post = post
            comment.parent = parent_comment
            comment.save()
            messages.success(request, 'کامنت شما با موفقیت ثبت شد و پس از تایید ادمین نمایش داده میشود.')
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(request, 'ثبت کامنت با خطا مواجه شد. لطفاً مجدداً تلاش کنید.')
    else:
        form = CommentForm()

    return render(request, 'page.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'social_links': social_links
    })
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'posts':posts})

def add_reply(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    parent_comment_id = request.POST.get('parent_id')
    parent_comment = get_object_or_404(Comment, id=parent_comment_id) if parent_comment_id else None

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.parent = parent_comment
            reply.save()
            return redirect('post_detail', pk=post.id)
    return redirect('post_detail', pk=post.id)