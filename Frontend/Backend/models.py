from django.db import models
from django.db.models.enums import Choices

class Contact(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=120)
    
    telephone=models.CharField(max_length=120)
    CHOICES = (
        ('IN', 'India'),
        ('US', 'United States'),
        ('FR', 'France'),
        ('CN', 'China'),
        ('RU', 'Russia'),
        ('IT', 'Italy'),
        ('OTH', 'Other'),
    )
    country = models.CharField(max_length=300, default="India",choices = CHOICES)
    Choices= (
        ("F","Female"),
        ("M","Male"),
        ("O","Other"),
    )
    gender = models.CharField(max_length=130,default="Male",choices= Choices)
    email=models.EmailField(max_length=120)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
       return self.name
    