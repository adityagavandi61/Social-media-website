from django.contrib import admin
from socialweb.models import UserRegister, ViewerRegister

# Register your models here.
# class UserRegister(admin.ModelAdmin):
#     list_display=('desc','post')

# admin.site.register(Post,Posts),
admin.site.register(ViewerRegister),
admin.site.register(UserRegister)