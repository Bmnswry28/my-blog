from django.contrib import admin
from .models import *
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publishedDate', 'status')
    search_fields = ('title', 'content')
    list_filter = ('status', 'created_at', 'publishedDate', 'author')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publishedDate']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_pic')
    search_fields = ('user__username', 'bio')
    list_filter = ('user',)