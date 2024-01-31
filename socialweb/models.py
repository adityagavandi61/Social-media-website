from django.db import models
from datetime import datetime

# Create your models here.
class ViewerRegister(models.Model):
    name=models.CharField(max_length=50)
    gmail=models.EmailField()
    password=models.CharField(max_length=8)
    
class UserRegister(models.Model):
    name = models.CharField(max_length=40)
    gmail = models.EmailField()
    address = models.CharField(max_length=50)
    page_name = models.CharField(max_length=100, default='Enter page name')
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=10)  
    bio=models.CharField(max_length=100, default='add bio') 
    profile_pic=models.FileField(upload_to="profile_pic/",max_length=250,null=True,default='profile_pic/profilepic.svg')


class Post(models.Model):
    caption=models.CharField(max_length=250)
    post=models.FileField(upload_to="posts/",max_length=250,null=True,default=None)