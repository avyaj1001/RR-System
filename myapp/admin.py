from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","product_name","product_image","category","price","product_description", "product_stat")

class SizeAdmin(admin.ModelAdmin):
    list_display = ("id","standard_size","height","width","length",)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ("id","product","color","size","price")

class ColorAdmin(admin.ModelAdmin):
    list_display = ("id","name")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","category_name")


    
admin.site.register(Category, CategoryAdmin)

admin.site.register(Order)
admin.site.register(Color, ColorAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Cart)
admin.site.register(contact)
admin.site.register(Product,ProductAdmin)

