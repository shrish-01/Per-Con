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
    path('emotional/' , views.emotional , name = 'emotional'),
    path('envy/' , views.envy , name = 'envy'),
    path('loneliness/' , views.loneliness , name = 'loneliness'),
    path('shyness/' , views.shyness , name = 'shyness'),
    path('copingwithpandemic/' , views.copingwithpandemic , name = 'copingwithpandemic'), 
    path('artofparenting/' , views.artofparenting , name = 'artofparenting'),
    path('managing/' , views.managing, name = 'managing'),
    path('contheartbreak/' , views.contheartbreak , name = 'contheartbreak'),
    path('test/' , views.test , name = 'test'),

]