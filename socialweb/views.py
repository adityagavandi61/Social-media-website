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
def home(request):
    user_object = CustomUser.objects.get(username=request.user.username)
    user_profile = Profile.objects.filter(user=user_object)
    post = Post.objects.all().order_by('-created_at')
    
    context={
        'user_object': user_object,
        'user_profile': user_profile,
        'post':post,
    }
    return render(request,'home.html',context)

@login_required(login_url='login')
def search(request):
    user=CustomUser.objects.get(id=request.user.id)
    profile=Profile.objects.all()
    context={
        'profile':profile,
    }
    return render(request,'search.html',context)

def account(request):
    return render(request,'myaccount.html')

@login_required(login_url='login')
def pagedetails(request,pk):
    user_object = CustomUser.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
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

            return redirect('editaccount')
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

            return redirect('home')
    return render(request,'viewerregister.html')


def viewerregister(request):
    return render(request, 'viewerregister.html')

@login_required(login_url='login')
def dashboard(request):
    user=CustomUser.objects.get(id=request.user.id)
    profile=Profile.objects.filter(user=user)

    follower = request.user.id
    user_followers = len(FollowersCount.objects.filter(user=user))

    context={
        'profile':profile,
        'user_followers': user_followers,
    }
    return render(request,'dashboardstatic.html',context)

@login_required(login_url='login')
def uploadpost(request):
    if request.method=='POST':
        user = request.user.username
        caption=request.POST.get('caption')
        content=request.FILES.get('content')
        
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
            )
            media.save()
            return redirect('dashboard')

    return render(request,'dashboardstatic.html')

@login_required(login_url='login')
def seepost(request):
    user=CustomUser.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    post = Post.objects.filter(profile=profile).order_by('-created_at')
    context={
        'profile': profile,
        'post':post,
    }
    return render(request,'dashboardpost.html',context)

@login_required(login_url='login')
def editaccount(request):
    user=CustomUser.objects.get(id=request.user.id)
    profile=Profile.objects.filter(user=user)
    context={
        'profile':profile,
    }
    return render(request,'dashboardeditaccount.html',context)

@login_required(login_url='login')
def profileupdate(request):
    if request.method == "POST":
        profile_pic=request.FILES.get('profile_pic')
        bio=request.POST.get('bio')
        username=request.POST.get('username')
        location=request.POST.get('location')
        
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.bio=bio
            customuser.profile_pic=profile_pic
            customuser.username=username
            customuser.location=location

            customuser.save()
            if username !=None and username !="":
                customuser.set_username(username)
            if profile_pic != None and profile_pic !="":
                customuser.set_profile_pic=profile_pic
            if bio !=None and bio !="":
                customuser.set_bio(bio)
            if location !=None and location !="":
                customuser.set_location(location)
            customuser.save()

            messages.success(request,'Profile Update Successfully.')
            return redirect('editaccount')
        except:
            messages.error(request,'Failed to update profile')
            return redirect('editaccount')
            

    return render(request,'dashboardeditaccount.html')


def useraccount(request):
    return render(request,'userac.html')

