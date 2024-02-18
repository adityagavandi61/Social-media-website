from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings
 
User = settings.AUTH_USER_MODEL
 
# create models here

class CustomUser(AbstractUser):
    user=((1,"viewer"),(2,'profile'))
    user_type = models.CharField(choices=user,max_length=255,default=1)
    profile_pic=models.ImageField(upload_to='profilepic',default="static/assets/svg/profile.svg")


class viewer(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name


class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    bio=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username+" "+" Created by @ "+self.user.first_name+" "+self.user.last_name

class Post(models.Model):
    user=models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    content = models.FileField(upload_to='post',null=True)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username