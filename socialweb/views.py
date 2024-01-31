from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from socialweb.models import UserRegister, ViewerRegister,Post
from socialweb.forms import UserRegisterForm, ViewerRegisterForm



def home(request):
    user=UserRegister.objects.all()
    post=Post.objects.all()
    return render(request,'home.html',{'User':user,'Post':post})

def search(request):
    user=UserRegister.objects.all()
    return render(request,'search.html',{'User':user})

def account(request):
    user=UserRegister.objects.all()
    return render(request,'myaccount.html',{'User':user})

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
    user=UserRegister.objects.all()
    return render(request,'dashboardstatic.html',{'User':user})

def seepost(request):
    user=UserRegister.objects.all()
    post=Post.objects.all()
    return render(request,'dashboardpost.html',{'User':user,'Post':post})

def editaccount(request):
    return render(request,'dashboardeditaccount.html')

def useraccount(request):
    user=UserRegister.objects.all()
    return render(request,'userac.html',{'User':user})

