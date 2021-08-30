from django.shortcuts import render,redirect
from django.http.response import HttpResponseNotAllowed
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import auth , User 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"index.html")
 
def about(request) :
    return render(request,"about.html")
     
@login_required(login_url='login')
def test(request) :
    return render(request,"test.html")

@login_required(login_url='login')
def contheartbreak(request) :
    return render(request,"contheartbreak.html")

@login_required(login_url='login')
def emotional(request) :
    return render(request,"emotional.html")

@login_required(login_url='login')
def envy(request) :
    return render(request,"envy.html")

@login_required(login_url='login')
def shyness(request) :
    return render(request,"shyness.html")

@login_required(login_url='login')
def loneliness(request) :
    return render(request,"loneliness.html")

@login_required(login_url='login')
def copingwithpandemic(request) :
    return render(request,"copingwithpandemic.html")

@login_required(login_url='login')
def managing(request) :
    return render(request,"managing.html")

@login_required(login_url='login')
def artofparenting(request) :
    return render(request,"artofparenting.html")


def contact(request) :
    if request.method == 'POST' :
      name = request.POST.get('name')
      email= request.POST.get('email')
      phone = request.POST.get('phone')
      content=request.POST.get('content')
      desc = request.POST.get('desc')
      
      contact =Contact(name=name,email=email,phone=phone,content=content,desc=desc,date= datetime.today())
      contact.save()
      messages.success(request, 'Your message has been sent!')
    return render(request,"contact.html")

def services(request) :
    return render(request,"services.html")
    
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            coun = request.POST['coun']
            gen = request.POST['gen']
            a = request.POST['a']
            
            
            if len(username)>10 and len(username)<5:
                messages.error(request,"Username must be under 10 characters and more than 5characters")
                return redirect('register')

            if password == password2 :
                if User.objects.filter(email=email).exists():
                    messages.info(request , 'Email already used')
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.info(request , 'Username Already Used' )
                    return redirect('register')
                else:
                    user = User.objects.create_user(email=email , username=username ,password=password)
                    user.name = name 
                    user.save();
                    messages.success(request,"Your account has been succesfully created !!!")
                    return redirect('/login')
            else:
                messages.info(request , 'Password is not same, try again !!!')
                return redirect('register')
        else:
                return render(request , 'register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
                loginusername = request.POST ['loginusername']
                loginpassword = request.POST['loginpassword']

                user = auth.authenticate(username=loginusername , password=loginpassword)

                if user is not None:
                        login(request , user)
                        messages.success(request,"Successfully logged in")
                        return redirect('/')
                else:
                    messages.info(request , 'invalid credentials, please try again')
                    return redirect('login')
        else: 
            return render ( request , 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def mental(request) :
    return render(request,"mental.html")

def physical(request) :
    return render(request,"physical.html")

def inspirational(request) :
    return render(request,"inspirational.html")

def anxiety(request) :
    return render(request,"anxiety.html")