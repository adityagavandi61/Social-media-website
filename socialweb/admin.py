from django.contrib import admin
from socialweb.models import UserRegister, ViewerRegister

# Register your models here.


admin.site.register(ViewerRegister),
admin.site.register(UserRegister)