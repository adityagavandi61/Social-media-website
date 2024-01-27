"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialweb import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Dashavatar SocialMediaWebsite Admin"
admin.site.site_title = "Dashavatar SocialMediaWebsite Admin Portal"
admin.site.index_title = "Welcome to Dashavatar SocialMediaWebsite"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('newac',views.newac,name='newac'),
    path('userregister',views.userregister,name='userregister'),
    path('viewerregister',views.viewerregister,name='viewerregister'),
    path('home',views.home, name='home'),
    path('search',views.search, name='search'),
    path('myaccount',views.account, name='account'),
    path('static',views.static, name='static'),
    path('editaccount',views.editaccount, name='editaccount'),
    path('seepost',views.seepost, name='seepost')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)