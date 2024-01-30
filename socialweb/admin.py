from django.contrib import admin
from socialweb.models import UserRegister, ViewerRegister,Post

# Register your models here.
class Posts(admin.ModelAdmin):
    list_display=('caption','post')

admin.site.register(Post,Posts),
admin.site.register(ViewerRegister),
admin.site.register(UserRegister)