from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product

# Create your views here.

def index(request):
    img_height = 800
    img_width = 800
    context = {
        'categories': Category.objects.all(),
        'img_height': img_height,
        'img_width': img_width
    }
    return render(request, "index.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def category_products(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category_products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'category_products': category_products
    }
    return render(request, "category_products.html", context)

def store(request):
    context = {}
    return render(request, "store.html", context)