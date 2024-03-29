from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404
from socialweb.emailhandle import EmailHandle
from socialweb.models import *
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from itertools import chain
import random

def login(request):
    return render(request,'login.html')

def dologin(request):
    if request.method == 'POST':
        user = EmailHandle.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            auth_login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('/')
            elif user_type == '2':
                return redirect('dashboard')
        else:
            messages.error(request, 'Email and Password are Invalid')
            return render(request,'login.html')
    
    else:
        messages.error(request, 'Email and Password are Invalid')
        return render(request,'login.html')

@login_required(login_url='login')
def dologout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def likepost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')

@login_required(login_url='login')
def plikepost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('postview/'+post_id)
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('postview/'+post_id)

@login_required(login_url='login')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete() 
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')

@login_required(login_url='login')
def comment(request):
    if request.method == 'POST':
        user = request.POST['user']
        post_id = request.POST['post_id']
        comment = request.POST['comment']

        if comment:
            newcomment=CommentPost.objects.create(user=user, post_id=post_id,comment=comment)
            newcomment.save()
            return redirect('/')
        else:
            messages.error(request, "Leave a comment")
            return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='login')
def pcomment(request):
    if request.method == 'POST':
        user = request.POST['user']
        post_id = request.POST['post_id']
        comment = request.POST['comment']

        if comment:
            newcomment=CommentPost.objects.create(user=user, post_id=post_id,comment=comment)
            newcomment.save()
            return redirect('postview/'+post_id)
        else:
            messages.error(request, "Leave a comment")
            return redirect('postview/'+post_id)
    else:
        return redirect('/')

@login_required(login_url='login')
def pshare(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    Share_filter = SharePost.objects.filter(post_id=post_id, username=username).first()

    if Share_filter == None:
        new_like = SharePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_share = post.no_of_share+1
        post.save()
        return redirect('postview/'+post_id)
    else:
        return redirect('postview/'+post_id)

@login_required(login_url='login')
def share(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    Share_filter = SharePost.objects.filter(post_id=post_id, username=username).first()

    if Share_filter == None:
        new_like = SharePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_share = post.no_of_share+1
        post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='login')   
def postview(request,id):
    user_posts = Post.objects.get(id=id)
    postlike = len(LikePost.objects.filter(post_id=id))
    sharepost = len(SharePost.objects.filter(post_id=id))
    post_comments = CommentPost.objects.filter(post_id=id).order_by('-created_at')
    lencom=len(post_comments)
    context = {
        'user_posts': user_posts,
        'post_comments': post_comments,
        'lencom':lencom,
        'postlike':postlike,
        'sharepost':sharepost,
    }

    return render(request,'postview.html',context)

@login_required(login_url='login')
def home(request):
    user_object = CustomUser.objects.get(username=request.user.username)
    user_profile = Profile.objects.filter(user=user_object)
    post = Post.objects.all().order_by('-created_at')
    

    context={
        'user_object': user_object,
        'user_profile': user_profile,
        'post':post,
    }

    if user_object.user_type =='2':
        return redirect('dashboard')

    return render(request,'home.html',context)

@login_required(login_url='login')
def usersearch(request):
    user=CustomUser.objects.get(username=request.user.username)

    if request.method == 'GET':
        username=request.GET['username']
        profile=CustomUser.objects.filter(username__contains=username)

        len_profile=len(profile)

        if username == "":
            return redirect('search')
    
    if user.user_type =='2':
        return redirect('dashboard')   
    context={
        'username':username,
        'profile':profile,
        'len_profile':len_profile,
    }
    return render(request,'searchuser.html',context)

@login_required(login_url='login')
def search(request):
    user_object=CustomUser.objects.get(username=request.user.username)
    profile=Profile.objects.filter(user=user_object)

    user_follower = FollowersCount.objects.filter(follower=user_object)
    user_followers = len(FollowersCount.objects.filter(follower=user_object))


    context={
        'user_object': user_object,
        'profile':profile,
        'user_follower': user_follower,
        'user_followers': user_followers,
    }
    if user_object.user_type =='2':
        return redirect('dashboard')


    return render(request,'search.html',context)

@login_required(login_url='login')
def account(request):
    user=request.user
    user_object=CustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        profile_pic=request.FILES.get('profile_pic')
        
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.profile_pic=profile_pic

            customuser.save()
            if profile_pic != None and profile_pic !="":
                customuser.set_profile_pic=profile_pic
            customuser.save()

            messages.success(request,'Profile Update Successfully.')
            return redirect('account')
        except:
            messages.error(request,'Failed to update profile')
            return redirect('account')
    if user_object.user_type =='2':
        return redirect('dashboard')
    
    return render(request,'myaccount.html')

@login_required(login_url='login')
def pagedetails(request,pk):
    user_object = CustomUser.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk).order_by('-created_at')
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
    }

    return render(request,'pagedetails.html',context)
  
def newac(request):
    return render(request,'newac.html')

def adduser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        location=request.POST.get('location')
        bio=request.POST.get('bio')
        profile_pic=request.FILES.get('profile_pic')
        password=request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already taken')
            return redirect('userregister')
        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()


            profile=Profile(
                user = user,
                location = location,
                bio = bio
            )
            profile.save()

            user = EmailHandle.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
            if user is not None:
                auth_login(request, user)
                user_type = user.user_type
                if user_type == '1':
                    return redirect('/')
                elif user_type == '2':
                    return redirect('dashboard')
    return render(request, 'userregister.html')

def userregister(request):
    return render(request, 'userregister.html')

def addviewer(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        profile_pic=request.FILES.get('profile_pic')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already taken')
            return redirect('viewerregister')
        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                profile_pic=profile_pic,
                email=email,
                user_type=1
            )
            user.set_password(password)
            user.save()
            Viewer=viewer(
                user = user,
            )
            Viewer.save()
            user = EmailHandle.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
            if user is not None:
                auth_login(request, user)
                user_type = user.user_type
                if user_type == '1':
                    return redirect('/')
                elif user_type == '2':
                    return redirect('dashboard')
    return render(request,'viewerregister.html')

def viewerregister(request):
    return render(request, 'viewerregister.html')

@login_required(login_url='login')
def dashboard(request):
    user=CustomUser.objects.get(id=request.user.id)
    profile=Profile.objects.filter(user=user)

    user_follower = FollowersCount.objects.filter(user=user).order_by('follower').reverse()
    user_followers = len(FollowersCount.objects.filter(user=user))


    user_posts = Post.objects.filter(user=user).order_by('-created_at')
    postlikes = LikePost.objects.filter(post_id=id)
    shareposts = SharePost.objects.filter(post_id=id)
    postlike = len(LikePost.objects.filter(post_id=id))
    sharepost = len(SharePost.objects.filter(post_id=id))
        
    context={
        'profile':profile,
        'user_follower': user_follower,
        'user_followers': user_followers,
        'user_posts': user_posts,
        'postlike':postlike,
        'postlikes':postlikes,
        'sharepost':sharepost,
        'shareposts':shareposts,
    }

    if user.user_type =='1':
        return redirect('/')

    return render(request,'dashboardstatic.html',context)

@login_required(login_url='login')
def uploadpost(request):
    if request.method=='POST':
        user = request.user.username
        caption=request.POST.get('caption')
        content=request.FILES.get('content')
        video=request.FILES.get('video')
        
        if content == None:
            messages.warning(request,'Select Media')
            return redirect('dashboard')
        else:
            profile=Profile.objects.get(user=request.user.id)
            media=Post(
                user=user,
                profile=profile,
                caption=caption,
                content=content,
                video=video,
            )
            media.save()
            return redirect('dashboard')

    return render(request,'dashboardstatic.html')

@login_required(login_url='login')
def uploadvideo(request):
    if request.method=='POST':
        user = request.user.username
        caption=request.POST.get('caption')
        video=request.FILES.get('video')
        
        if video == None:
            messages.warning(request,'Select Media')
            return redirect('dashboard')
        else:
            profile=Profile.objects.get(user=request.user.id)
            media=Post(
                user=user,
                profile=profile,
                caption=caption,
                video=video,
            )
            media.save()
            return redirect('dashboard')

    return render(request,'dashboardstatic.html')

@login_required(login_url='login')
def seepost(request):
    user=CustomUser.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    post = Post.objects.filter(profile=profile).order_by('-created_at')
    lenpost=len(Post.objects.filter(profile=profile))
    context={
        'profile': profile,
        'post':post,
        'lenpost':lenpost,
    }

    if user.user_type =='1':
        return redirect('/')


    return render(request,'dashboardpost.html',context)

@login_required(login_url='login')
def editaccount(request):
    user=CustomUser.objects.get(id=request.user.id)
    profile=Profile.objects.filter(user=user)
    context={
        'profile':profile,
    }

    if user.user_type =='1':
        return redirect('/')

    return render(request,'dashboardeditaccount.html',context)

@login_required(login_url='login')
def profileupdate(request):
    if request.method == "POST":
        customuser=CustomUser.objects.get(id=request.user.id)
        profile = Profile.objects.get(user_id=request.user.id)
        bio = request.POST.get('bio')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        youtube = request.POST.get('youtube')

        if bio ==None or bio=="":
            profile.set_bio = bio
            profile.save()

        if facebook ==None or facebook=="":
            profile.set_facebook = facebook
            profile.save()

        if instagram ==None or instagram=="":
            profile.set_instagram = instagram
            profile.save()

        if youtube ==None or youtube=="":
            profile.set_youtube = youtube
            profile.save()


        profile.bio = bio
        profile.facebook = facebook
        profile.instagram = instagram
        profile.youtube = youtube
        profile.save()

    if request.method == "POST":
        customuser=CustomUser.objects.get(id=request.user.id)
        profile_pic=request.FILES.get('profile_pic')
        

        if profile_pic == None and profile_pic =="":
                customuser.set_profile_pic=profile_pic
                customuser.save()

        customuser.profile_pic=profile_pic
        customuser.save()
        return redirect('editaccount')      

    return render(request,'dashboardeditaccount.html')

@login_required(login_url='login')
def userpost(request,id):
    user=CustomUser.objects.get(id=request.user.id)
    user_posts = Post.objects.get(id=id)
    postlikes = LikePost.objects.filter(post_id=id)
    shareposts = SharePost.objects.filter(post_id=id)
    postlike = len(LikePost.objects.filter(post_id=id))
    sharepost = len(SharePost.objects.filter(post_id=id))
    post_comments = CommentPost.objects.filter(post_id=id).order_by('-created_at')
    lencom=len(post_comments)

    if request.method == 'POST':
        user_posts.delete()
        return redirect('dashboard')

    context = {
        'user_posts': user_posts,
        'post_comments': post_comments,
        'lencom':lencom,
        'postlike':postlike,
        'postlikes':postlikes,
        'sharepost':sharepost,
        'shareposts':shareposts,
    }
    if user.user_type =='1':
        return redirect('/')
    return render(request,'userpost.html',context)
    