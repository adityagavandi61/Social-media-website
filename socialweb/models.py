from django.db import models
from django.contrib.auth.models import AbstractUser

# create models here

class CustomUser(AbstractUser):
    user=((1,'viewer'),(2,'profile'))
    user_type = models.CharField(choices=user,max_length=255,default=1)
    profile_pic=models.ImageField(upload_to='profilepic',default="static/assets/svg/profile.svg")