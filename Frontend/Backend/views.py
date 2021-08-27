from django.shortcuts import render,redirect
from django.http.response import HttpResponseNotAllowed
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import auth , User

def home(request):
    return render(request,"index.html")
 
def about(request) :
    return render(request,"about.html")
    
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request , 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request , 'Username Already Used' )
                return redirect('register')
            else:
                user = User.objects.create_user(name=name,email=email , username=username ,password=password   )
                user.save();
                return redirect('/login')
        else:
            messages.info(request , 'Password is not same')
            return redirect('register')
    else:
        return render(request , 'register.html')

def login(request):
  if request.method == 'POST':
           username = request.POST ['username']
           password = request.POST['password']

           user = auth.authenticate(username=username , password=password)

           if user is not None:
                 auth.login(request , user)
                 return redirect('/')
           else:
            messages.info(request , 'invalid')
            return redirect('login')
            
  else: 
             return render ( request , 'login.html')
   
