from django.contrib import admin
from .models import Contact, Food

# Register your models here.
admin.site.register(Food)
admin.site.register(Contact)