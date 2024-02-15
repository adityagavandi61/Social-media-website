from django.contrib import admin
from socialweb.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# class Posts(admin.ModelAdmin):
#     list_display=('post_id','caption')

class UserModel(UserAdmin):
    list_display=('username','user_type','profile_pic')

admin.site.register(CustomUser,UserModel)

admin.site.register(viewer),
admin.site.register(Profile),
admin.site.register(Post)
# admin.site.register(LikePost),
# admin.site.register(FollowersCount)