from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('search', search_results, name='search_results'),
    path('categories/', category_list, name='category_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('about', AboutView, name='about'),
    path('titles', post_titles_view, name='post_titles'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/reply/', add_reply, name='add_reply'),
    path('captcha/', include('captcha.urls')),
]
