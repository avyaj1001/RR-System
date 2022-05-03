
from unicodedata import category
from django.db import models
from .models import *

# Create your models here.


class contact (models.Model):
    full_name = models.CharField (max_length=100)
    phone_num = models.CharField (max_length=13)
    email = models.CharField  (max_length=100)
    message = models.TextField ()

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Color (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Size (models.Model):
    height = models.IntegerField(null= True, blank = True)
    width = models.IntegerField(null= True, blank = True)
    length = models.IntegerField(null= True, blank = True)
    standard_size = models.CharField (max_length=100,null = True, blank = True)

    def __str__(self):
        return self.standard_size


class Product (models.Model):
    Status = (
        ('In Stock', 'In Stock'),
        ('Out of Stock','Out of Stock')
    )
    product_image = models.ImageField(upload_to='image',blank=True)
    product_name = models.CharField (max_length=100, null=True)
    product_description = models.TextField( blank=True)
    price = models.IntegerField( null= True, blank= True)
    product_quantity = models.CharField(max_length=10000, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True,blank=True, related_name="products")
    product_stat = models.CharField(max_length=50, choices=Status,null = True)

    def __str__(self):
        return self.product_name

class ProductAttribute (models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

class Order (models.Model):
    Status =(
        ('PENDING', 'PENDING'),
        ('COMPLETED','COMPLETED')
    )
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    total_amount = models.IntegerField()
    status = models.CharField(max_length=100, choices=Status, null = True)

class Cart (models.Model):
    product = models.ForeignKey(Product, null=True,on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True,on_delete=models.CASCADE)
    quantity = models.IntegerField(default="1")
    total_amount = models.IntegerField()