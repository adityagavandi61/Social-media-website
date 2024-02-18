from django.contrib import admin
from socialweb.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class Posts(admin.ModelAdmin):
    list_display=('user','created_at')

class UserModel(UserAdmin):
    list_display=('username','user_type')

admin.site.register(CustomUser,UserModel)

admin.site.register(viewer),
admin.site.register(Profile),
admin.site.register(Post,Posts)
# admin.site.register(LikePost),
# admin.site.register(FollowersCount)