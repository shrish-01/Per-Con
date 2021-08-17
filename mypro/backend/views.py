
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request,"index.html")
 
def about(request) :
    return render(request,"about.html")
    
def contact(request) :
    return render(request,"contact.html")
   
def services(request) :
    return render(request,"services.html")
   