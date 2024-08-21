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