from django.contrib import admin
from media.models import Post
# Register your models here.
class Posts(admin.ModelAdmin):
    list_display=('caption','media')

admin.site.register(Post,Posts)
