from django.contrib import admin
from django.urls import path
from Backend import views
urlpatterns = [
    path('',views.home, name='home') ,
    path('about',views.about, name='about') ,
    path('contact',views.contact, name='contact') ,
    path('services',views.services, name='services') ,
]