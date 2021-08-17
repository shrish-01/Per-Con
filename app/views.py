
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

#create views here

def index(request):
    return HttpResponse("hello")

def about(request):
    return HttpResponse("About us")
     
def contact(request):
    
    return render(request,'mypro/contact.html')

