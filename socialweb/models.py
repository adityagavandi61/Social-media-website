from django.db import models
from django.contrib.auth.models import AbstractUser

# create models here

class CustomUser(AbstractUser):
    user=((1,'viewer'),(2,'profile'))
    user_type = models.IntegerField(choices=user, default=1)
    profile_pic=models.ImageField(upload_to='profilepic',default="static/svg/profile.svg")