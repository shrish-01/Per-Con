from django.db import models
class Contact(models.Model):
    fname=models.CharField(max_length=120)
    lname=models.CharField(max_length=120)
    sub=models.CharField(max_length=500)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    desc=models.TextField()
    date=models.DateField()
def __str__(self):
 return self.name
    