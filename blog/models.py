from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class posts(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    publishedDate=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    catgory=models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
    comments=models.IntegerField(default=0)
    image=models.ImageField('post_images/',null=True,blank=True)
    video=models.FileField("post_videos/",null=True,blank=True)
    def __str__(self):
        return self.title
class comments(models.Model):
    post=models.ForeignKey(posts,on_delete=models.CASCADE)
    comment_text=models.TextField()
    comment_date=models.DateTimeField(timezone.now)
    user_name = models.CharField(max_length=80)
    email=models.EmailField(null=True,blank=True)
    website=models.URLField(null=True,blank=True)
    image = models.ImageField(upload_to='comment_images/', null=True, blank=True)  
    video = models.FileField(upload_to='comment_video/',null=True,blank=True)
    def __str__(self):
        return self.comment_text