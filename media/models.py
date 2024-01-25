from django.db import models

# Create your models here.
class Post(models.Model):
    caption=models.CharField(max_length=250)
    media=models.FileField(upload_to="posts/",max_length=250,null=True,default=None)