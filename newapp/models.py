from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    image=models.FileField(upload_to='image',null=True,blank=True)


class Product(models.Model):
    product_category = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='image', null=True, blank=True)
    product_price = models.IntegerField()
    product_discound = models.IntegerField()
    product_description = models.CharField(max_length=255)
    product_stock = models.IntegerField()
    product_IsAvailable = models.BooleanField(default=True)
    product_createdAt = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.IntegerField()

 