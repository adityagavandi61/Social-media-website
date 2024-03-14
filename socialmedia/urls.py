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
    path('login',views.login,name='login'),
    path('do',views.dologin,name='dologin'),
    path('dologout',views.dologout,name='logout'),
    path('newac',views.newac,name='newac'),
    path('userregister',views.userregister,name='userregister'),
    path('adduser',views.adduser,name='adduser'),
    path('profile/<str:pk>',views.pagedetails,name='pagedetails'),
    path('addviewer',views.addviewer,name='addviewer'),
    path('viewerregister',views.viewerregister,name='viewerregister'),
    path('',views.home, name='home'),
    path('search',views.search, name='search'),
    path('myaccount',views.account, name='account'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('uploadpost',views.uploadpost, name='uploadpost'),
    path('likepost',views.likepost, name='likepost'),
    path('plikepost',views.plikepost, name='plikepost'),
    path('follow',views.follow, name='follow'),
    path('comment',views.comment, name='comment'),
    path('pcomment',views.pcomment, name='pcomment'),
    path('share',views.share, name='share'),
    path('pshare',views.pshare, name='pshare'),
    path('postview/<str:id>',views.postview, name='postview'),
    path('editaccount',views.editaccount, name='editaccount'),
    path('profileupdate',views.profileupdate, name='profileupdate'),
    path('seepost',views.seepost, name='seepost'),
    path('userpost/<str:id>',views.userpost, name='userpost')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)