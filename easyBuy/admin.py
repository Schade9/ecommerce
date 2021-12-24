from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'image'
    )
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'productName', 'productPrice', 'category', 'skuNumber', 'description', 'condition', 'warranty', 'image'
    )
admin.site.register(Product, ProductAdmin)
