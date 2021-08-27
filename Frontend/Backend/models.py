from django.db import models
from django.db.models.enums import Choices

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=120)
    phone=models.CharField(max_length=120)
    CHOICES = (
        ('RL', 'Relationship'),
        ('LC', 'Life Coaching'),
        ('LR', 'Leadership'),
        ('TM', 'Team Managament'),
    
    )
    content = models.CharField(max_length=300, default="Life coaching",choices = CHOICES)
   
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
       return self.name
    