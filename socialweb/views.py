from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserRegister, ViewerRegister
from .forms import UserRegisterForm, ViewerRegisterForm


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
    
def newac(request):
    return render(request,'newac.html')

def userregister(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           user = UserRegister.objects.create(
                name=request.POST['name'],
                gmail=request.POST['gmail'],
                address=request.POST['address'],
                page_name=request.POST['page_name'],
                phone_number=request.POST['phone_number'],
                password=request.POST['password']
            )
    else:
        form = UserRegisterForm()

    return render(request, 'userregister.html')

def viewerregister(request):
    if request.method=="POST":
        form = ViewerRegisterForm(request.POST)
        if form.is_valid():
            viewer = ViewerRegister.objects.create(
                name=request.POST['name'],
                gmail=request.POST['gmail'],
                password=request.POST['password']
            )
    else:
        form = ViewerRegisterForm()

    return render(request, 'viewerregister.html')

def dashboard(request):
    return render(request,'dashboard.html')
