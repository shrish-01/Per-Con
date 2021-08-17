from django.http import HttpResponse
from django.shortcuts import render
from .models import *

#create views here

def index(request):
    return HttpResponse("hello")

def about(request):
    return HttpResponse("About us")
     
def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name,phone,email,desc)
        contact = Contact(name=name,phone=phone,desc=desc,email=email)
        contact.save()
    return render(request,'mypro/contact.html')