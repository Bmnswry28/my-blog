from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('search', search_results, name='search_results'),
    path('archive', archive_view, name='archive_list'),
    path('about', AboutView, name='about'),
    path('titles', post_titles_view, name='post_titles'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]
