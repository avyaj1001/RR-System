
import email
from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name
    


class contact (models.Model):
    full_name = models.CharField (max_length=100)
    phone_num = models.CharField (max_length=13)
    email = models.CharField  (max_length=100)
    message = models.TextField ()


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    zipcode = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_name = models.CharField(max_length=100)



    def __str__(self):
        return self.category_name

class Window(Category):
    size2 = '4 x 6'
    size3 = '6 x 8'
    SIZE_CHOICES = (
        (size2, '4 x 6'),
        (size3, '6 x 8'),
    )
    
    standard_size = models.CharField(choices= SIZE_CHOICES,max_length=100, null=True, blank = True)

class Door(Category):
    standard_size = models.CharField(max_length=100, null=True, blank = True)

class Aquarium(Category):
    standard_size = models.CharField(max_length=100, null=True, blank = True)



class Hanging_Cabinet (Category):
    standard_size = models.CharField(max_length=100, null=True, blank = True)

class Build_in_Cabinet(Category):
    standard_size = models.CharField(max_length=100, null=True, blank = True)

class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types
    of productsr that are for sale.
    """

    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

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
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order (models.Model):
    Status =(
        ('PENDING', 'PENDING'),
        ('COMPLETED','COMPLETED')
    )
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    total_amount = models.IntegerField()
    status = models.CharField(max_length=100, choices=Status, null = True)
