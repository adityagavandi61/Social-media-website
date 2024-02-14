from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from datetime import datetime
from django.contrib import messages
from socialweb.emailhandle import EmailHandle
from socialweb.models import *
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth import login as auth_login

def login(request):
    return render(request,'login.html')

def dologin(request):
    if request.method == 'POST':
        # user_type = request.POST.get('user_type')
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
                return redirect('login')
    
    else:
        messages.error(request, 'Email and Password are Invalid')
        return render(request,'login.html')


def dologout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='/')
def home(request):
    return render(request,'home.html')

def search(request):
    return render(request,'search.html')

def account(request):
    return render(request,'myaccount.html')


def pagedetails(request):
    return render(request,'pagedetails.html')
  
def newac(request):
    return render(request,'newac.html')

def userregister(request):
    return render(request, 'userregister.html')

def viewerregister(request):
    return render(request, 'viewerregister.html')

def dashboard(request):
    return render(request,'dashboardstatic.html')

def seepost(request):
    return render(request,'dashboardpost.html')

def editaccount(request):
    user=CustomUser.objects.get(id=request.user.id)
    context={
        "user":user,
    }
    return render(request,'dashboardeditaccount.html',context)

def profileupdate(request):
    if request.method == "POST":
        profile_pic=request.FILES.get('profile_pic')
        bio=request.POST.get('bio')
        username=request.POST.get('username')
        location=request.POST.get('location')
        print(profile_pic)
        
        try:
            customuser=CustomUser.objects.get(id=request.user.id)

            customuser.bio=bio
            customuser.profile_pic=profile_pic
            customuser.username=username
            customuser.location=location

            if username !=None and username !="":
                customuser.set_username(username)
            if profile_pic !=None and profile_pic !="":
                customuser.set_profile_pic(profile_pic)
            if bio !=None and bio !="":
                customuser.set_bio(bio)
            if location !=None and location !="":
                customuser.set_location(location)

            customuser.svae()
            messages.success(request,'Profile Update Successfully.')
            redirect('/dashboardeditaccount')
        except:
            messages.error(request,'Failed to update profile')

    return render(request,'dashboardeditaccount.html')


def useraccount(request):
    return render(request,'userac.html')

