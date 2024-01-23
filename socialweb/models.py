from django.db import models

# Create your models here.
class ViewerRegister(models.Model):
    name=models.CharField(max_length=50)
    gmail=models.EmailField()
    password=models.CharField(max_length=8)
    class meta:
        db_table="viewerregister"

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    gmail = models.EmailField()
    address = models.CharField(max_length=255)
    page_name = models.CharField(max_length=100, default='default_value')
    phone_number = models.CharField(max_length=15,default='default_value')
    password = models.CharField(max_length=255)
    class meta:
        db_table="userregister"