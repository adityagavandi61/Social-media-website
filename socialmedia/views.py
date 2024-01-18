#created by me

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
    
def newac(request):
    return render(request,'newac.html')

def userregister(request):
    return render(request,'userregister.html')

def viewerregister(request):
    return render(request,'viewerregister.html')

def dashboard(request):
    return render(request,'dashboard.html')