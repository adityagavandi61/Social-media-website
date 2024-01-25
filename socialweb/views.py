from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from socialweb.models import UserRegister, ViewerRegister
from socialweb.forms import UserRegisterForm, ViewerRegisterForm


def home(request):
    return render(request,'home.html')

def search(request):
    return render(request,'search.html')

def login(request):
    if request.method == "POST":
        gmail=request.POST['gmail'],
        password=request.POST['password'],
        user=authenticate(gmail=gmail,password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponse("account created")
        else:
            return HttpResponse("username and password incorrect")

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
        return HttpResponseRedirect('/dashboard')
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
        return HttpResponseRedirect('/home')
    else:
        form = ViewerRegisterForm()

    return render(request, 'viewerregister.html')

def dashboard(request):
    return render(request,'dashboard.html')

