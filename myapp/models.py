from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size_choices = (
        ('xsmall', 'XS'),
        ('small', 'S'),
        ('medium', 'M'),
        ('large', 'L'),
        ('xlarge', 'XL'),
        ('xxlarge', 'XXL'),
    )
    category_choices = (
        ('Shirts', 'Shirts'),
        ('Pants', 'Pants'),
        ('Innerwear', 'Innerwear'),
        ('Jeans', 'Jeans'),
        ('Jackets', 'Jackets'),
        ('Socks', 'Socks'),
        ('Wallets', 'Wallets'),
        ('Belts', 'Belts'),
        ('Ties', 'Ties'),
        ('Kerchiefs', 'Kerchiefs'),
        ('Tabs', 'Tabs'),
        ('Headphones', 'Headphones'),
        ('Cables', 'Cables'),
        ('Necklaces', 'Necklaces'),
        ('Rings', 'Rings'),
        ('Bracelets', 'Bracelets'),
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Biography', 'Biography'),
    )
    banner = models.ImageField(default='fallback.png', blank=True, upload_to='uploads/')
    category = models.CharField(max_length=100, default='category', choices=category_choices)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100, choices=size_choices, blank=True)

    def __str__(self):
        return f"{self.category} - {self.user.username}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)