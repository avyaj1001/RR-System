from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","product_name","product_image","category","price","product_description", "product_stat")

class SizeAdmin(admin.ModelAdmin):
    list_display = ("id","standard_size","height","width","length",)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ("product","color","price")

class ColorAdmin(admin.ModelAdmin):
    list_display = ("id","name")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","category_name")

class ProductTypeSpecificationAdmin (admin.ModelAdmin):
    list_display = ("id", "color", "size","name")

class WindowAdmin (admin.ModelAdmin):
    list_display = ("category_name","standard_size")

class DoorAdmin (admin.ModelAdmin):
    list_display = ("category_name","standard_size")



class AquariumAdmin (admin.ModelAdmin):
    list_display = ("category_name","standard_size")

class Hanging_CabinetAdmin (admin.ModelAdmin):
    list_display = ("category_name","standard_size")

class BuildinCabinetAdmin (admin.ModelAdmin):
    list_display = ("category_name","standard_size")

admin.site.register(Category, CategoryAdmin)

admin.site.register(Order)
admin.site.register(Color, ColorAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(contact)
admin.site.register(Profile)
admin.site.register(Product,ProductAdmin)
admin.site.register(Window,WindowAdmin)
admin.site.register(Door,DoorAdmin )
admin.site.register(Aquarium,AquariumAdmin )
admin.site.register(Hanging_Cabinet,Hanging_CabinetAdmin)
admin.site.register(Build_in_Cabinet,BuildinCabinetAdmin)



