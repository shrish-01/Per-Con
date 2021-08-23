from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=120)
    phone=models.CharField(max_length=120)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
       return self.name
    