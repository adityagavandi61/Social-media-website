from django.contrib import admin
from socialweb.models import UserRegister, ViewerRegister,Post

# Register your models here.
class Posts(admin.ModelAdmin):
    list_display=('caption','post','date')

class UserRegisters(admin.ModelAdmin):
    list_display=('name','gmail','phone_number','page_name','password','date')

class ViewerRegisters(admin.ModelAdmin):
    list_display=('name','gmail','password','date')

admin.site.register(Post,Posts),
admin.site.register(ViewerRegister,ViewerRegisters),
admin.site.register(UserRegister,UserRegisters)