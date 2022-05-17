from django.db import models
from myapp.models import *
# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)

    def _unicode__(self):
        return self.product.name
class Cart (models.Model):
    items = models.ManyToManyField(CartItem, null=True, blank=True)
    order = models.ForeignKey(Order, null=True,on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

