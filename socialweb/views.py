from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime 
from .forms import UserRegisterForm,ViewerRegisterForm


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
    
def newac(request):
    return render(request,'newac.html')

def userregister(request):
    if request.method == "POST":
        userform = UserRegisterForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('success') 
    else:
        userform = UserRegisterForm()

    return render(request, 'userregister.html', {'form': userform})

def viewerregister(request):
    if request.method=="POST":
        viewerform = ViewerRegisterForm(request.POST)
        if viewerform.is_valid():
            viewerform.save() 
            return redirect('success')
    else:
        viewerform = ViewerRegisterForm()

    return render(request, 'viewerregister.html', {'form': viewerform})

def dashboard(request):
    return render(request,'dashboard.html')
