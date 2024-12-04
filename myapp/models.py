from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    image = models.ImageField(upload_to='pics');  
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)