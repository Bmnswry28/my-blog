from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,null=True,blank=True)
    profile_pic=models.ImageField('profile_images/',null=True,blank=True)
    def __str__(self):
        return self.user.username
class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    Content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publishedDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catgory = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, related_name='posts')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    video = models.FileField(upload_to="post_videos/", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Link(models.Model):
    link_title=models.CharField(max_length=255)
    link_url=models.URLField()
    def __str__(self):
        return self.link_title
class Archive(models.Model):
    month=models.IntegerField()
    year=models.IntegerField()
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='comment_images/', blank=True, null=True)
    video = models.FileField(
        upload_to='comment_videos/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'