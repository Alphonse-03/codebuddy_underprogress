from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Java,Cpp,Python,Django,C,Javascript
# Create your views here.
def intro(request):
    return render(request,"intro.html")
def login(request):
    if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']

            user=auth.authenticate(username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect("listoc")

            else:
                messages.info(request,"You are not a reistered member please register and then login")
                return redirect("login")   
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        username=request.POST['uname']
        password=request.POST['password1']
        confirm=request.POST['password2']

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=f_name,last_name=l_name,password=password,username=username)
                user.save();
                return redirect("login")

        else:
            messages.info(request,"password is not matching")
       
            
                

    return render(request,"register.html")

    
def listoc(request):
    return render(request,"listoc.html")






def javaquiz(request):
    java=Java.objects.all()
    if request.method == 'POST':
        option=request.POST.get(1)
        print(option)
        
        print(Java.option_correct)
    return render(request,"index.html",{"questions":java,"name":1})











def cppquiz(request):
    cpp=Cpp.objects.all()
    if request.method == 'POST':
        option=request.POST.get('1')
        # print(request.POST.get('a'))
        print(option)
        print(Cpp.option_correct)
    return render(request,"index.html",{"questions":cpp,"name":1})





def javascriptquiz(request):
    javascript=Java.objects.all()
    if request.method == 'POST':
        option=request.POST.get('1')
        # print(request.POST.get('a'))
        print(option)
        print("hy")
    return render(request,"index.html",{"questions":javascript,"name":1})

def cquiz(request):
    c=C.objects.all()
    if request.method == 'POST':
        option=request.POST.get('1')
        # print(request.POST.get('a'))
        print(option)
        print("hy")
    return render(request,"index.html",{"questions":c,"name":1})
def pythonquiz(request):
    python=Python.objects.all()
    if request.method == 'POST':
        option=request.POST.get('1')
        # print(request.POST.get('a'))
        print(option)
        print("hy")
    return render(request,"index.html",{"questions":python,"name":1})

def djangoquiz(request):
    cpp=Django.objects.all()
    if request.method == 'POST':
        option=request.POST.get('1')
        # print(request.POST.get('a'))
        print(option)
        print("hy")
    return render(request,"index.html",{"questions":django,"name":1})
