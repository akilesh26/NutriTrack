from django.contrib import admin
from .models import user_item, Contact

# Register your models here.
admin.site.register(user_item)
admin.site.register(Contact)