from django.contrib import admin
from django.urls import path
from Backend import views



urlpatterns = [
    path("",views.home, name='home') ,
    path("home/",views.home, name='home') ,
    path("about/",views.about, name='about') ,
    path("contact/",views.contact, name='contact') ,
    path("services/",views.services, name='services') ,
    path('lin/' , views.lin , name = 'login'),
    path('lout/', views.lout, name="logout"),
    path('register/' , views.register , name = 'register'),
    path('about/lin' , views.lin , name = 'al'),
    path('about/register' , views.register , name = 'ar'),
    path('contact/lin' , views.lin , name = 'cl'),
    path('contact/register' , views.register , name = 'cr'),
    path('services/lin' , views.lin , name = 'sl'),
    path('services/register' , views.register , name = 'sr'),
    path('emotional/' , views.emotional , name = 'emotional'),
    path('envy/' , views.envy , name = 'envy'),
    path('loneliness/' , views.loneliness , name = 'loneliness'),
    path('shyness/' , views.shyness , name = 'shyness'),
    path('copingwithpandemic/' , views.copingwithpandemic , name = 'copingwithpandemic'), 
    path('artofparenting/' , views.artofparenting , name = 'artofparenting'),
    path('managing/' , views.managing, name = 'managing'),
    path('contheartbreak/' , views.contheartbreak , name = 'contheartbreak'),
    path('test/' , views.test , name = 'test'),
    path('mental/' , views.mental , name = 'mental'),
    path('physical/' , views.physical, name = 'physical'),
    path('inspirational/' , views.inspirational , name = 'inspirational'),
    path('anxiety/' , views.anxiety, name = 'anxiety'),
    
]