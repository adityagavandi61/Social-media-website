from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.conf import settings
import uuid

 
User = settings.AUTH_USER_MODEL
 
# create models here

class CustomUser(AbstractUser):
    user=((1,"viewer"),(2,'profile'))
    user_type = models.CharField(choices=user,max_length=255,default=1)
    profile_pic=models.FileField(upload_to='profilepic',null=True,default="/static/assets/svg/profile.svg")


class viewer(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name


class Profile(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    bio=models.TextField()
    facebook=models.URLField(max_length=300,null=True)
    instagram=models.URLField(max_length=300,null=True)
    youtube=models.URLField(max_length=300,null=True)
    created_at=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    profile=models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    content = models.FileField(upload_to='post',null=True)
    video = models.FileField(upload_to='post',null=True)
    user = models.CharField(max_length=100)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    no_of_share = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class CommentPost(models.Model):
    post_id = models.CharField(max_length=500)
    user = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user

class SharePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

