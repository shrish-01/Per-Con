from django.contrib import admin
from django.urls import path
from Backend import views
urlpatterns = [
    path("",views.home, name='home') ,
    path("home/",views.home, name='home') ,
    path("about/",views.about, name='about') ,
    path("contact/",views.contact, name='contact') ,
    path("services/",views.services, name='services') ,
    path('login/' , views.login , name = 'login'),
    path('register/' , views.register , name = 'register'),
    path('about/login' , views.login , name = 'al'),
    path('about/register' , views.register , name = 'ar'),
    path('contact/login' , views.login , name = 'cl'),
    path('contact/register' , views.register , name = 'cr'),
    path('services/login' , views.login , name = 'sl'),
    path('services/register' , views.register , name = 'sr'),
    
    

]