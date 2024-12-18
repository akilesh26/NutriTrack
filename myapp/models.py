from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100,default='Food Item')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nutrition = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)