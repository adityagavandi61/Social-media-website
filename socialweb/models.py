from django.db import models

# Create your models here.
class ViewerRegister(models.Model):
    name=models.CharField(max_length=50)
    gmail=models.EmailField()
    password=models.CharField(max_length=8)
    date=models.DateTimeField(null=True)
    
class UserRegister(models.Model):
    name = models.CharField(max_length=40,null=True)
    gmail = models.EmailField()
    address = models.CharField(max_length=50,null=True)
    page_name = models.CharField(max_length=100, default='Enter page name',null=True)
    phone_number = models.CharField(max_length=15,null=True)
    password = models.CharField(max_length=10,null=True)  
    bio=models.CharField(max_length=100, default='add bio',null=True) 
    profile_pic=models.FileField(upload_to="profile_pic/",max_length=250,null=True,default='profile_pic/profilepic.svg')
    date=models.DateTimeField(null=True)
    post=models.FileField(upload_to="posts/",max_length=250,null=True,default=None)

class Post(models.Model):
    caption=models.CharField(max_length=250,null=True)
    post=models.FileField(upload_to="posts/",max_length=250,null=True,default=None)
    date=models.DateTimeField(null=True)