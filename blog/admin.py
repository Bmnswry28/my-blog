from django.contrib import admin
from .models import Post, Category, Profile, SocialLink, Comment
from django.utils.html import format_html
# Registering Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publishedDate', 'status', 'is_published','catgory')
    search_fields = ('title', 'Content','catgory')
    list_filter = ('status', 'created_at', 'publishedDate', 'author')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publishedDate']
    empty_value_display = '-empty-'
    
    def is_published(self, obj):
        return obj.status == 'published'
    is_published.boolean = True
# Registering Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registering Profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_pic')
    search_fields = ('user__username', 'bio')
    list_filter = ('user',)

# Registering SocialLink model
admin.site.register(SocialLink)

# Registering Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'parent', 'created_at', 'is_published')
    search_fields = ('name', 'email', 'content')
    list_filter = ('created_at', 'is_published')
    ordering = ('created_at',)

    @admin.action(description='Publish selected comments')
    def publish_comments(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description='Unpublish selected comments')
    def unpublish_comments(self, request, queryset):
        queryset.update(is_published=False)

    actions = [publish_comments, unpublish_comments]

admin.site.register(Comment, CommentAdmin)