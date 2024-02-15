from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from datetime import datetime
from django.contrib import messages
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
                return redirect('home')
            elif user_type == '2':
                return redirect('dashboard')
        else:
            messages.error(request, 'Email and Password are Invalid')
            return render(request,'login.html')
    
    else:
        messages.error(request, 'Email and Password are Invalid')
        return render(request,'login.html')

@login_required(login_url='/')
def dologout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='/')
def home(request):
    user=CustomUser.objects.get(id=request.user.id)
    profile=Profile.objects.all()
    post=Post.objects.all()
    context={
        'profile':profile,
        'post':post,
    }
    return render(request,'home.html',context)

@login_required(login_url='/')
def search(request):
    profile=Profile.objects.all()
    context={
        'profile':profile,
    }
    return render(request,'search.html',context)

def account(request):
    return render(request,'myaccount.html')


def pagedetails(request):
    return render(request,'pagedetails.html')
  
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

@login_required(login_url='/')
def dashboard(request):
    user=CustomUser.objects.get(id=request.user.id)
    profile=Profile.objects.filter(user=user)
    context={
        'profile':profile,
    }
    return render(request,'dashboardstatic.html',context)

@login_required(login_url='/')
def uploadpost(request):
    if request.method=='POST':
        caption=request.POST.get('caption')
        content=request.FILES.get('content')
        
        if content == None:
            messages.warning(request,'Select Media')
            return redirect('dashboard')
        else:
            user=CustomUser.objects.get(id=request.user.id)
            media=Post(
                user=user,
                caption=caption,
                content=content,
            )
            media.save()
            return redirect('dashboard')

    return render(request,'dashboardstatic.html')

@login_required(login_url='/')
def seepost(request):
    post=Post.objects.all()
    context={
        'post':post,
    }
    return render(request,'dashboardpost.html',context)

@login_required(login_url='/')
def editaccount(request):
    user=CustomUser.objects.get(id=request.user.id)
    profile=Profile.objects.filter(user=user)
    context={
        'profile':profile,
    }
    return render(request,'dashboardeditaccount.html',context)

@login_required(login_url='/')
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

