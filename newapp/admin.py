from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Register, Product

admin.site.register(Register)
admin.site.register(Product)
