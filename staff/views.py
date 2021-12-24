from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from easyBuy.models import Category
from .forms import CreateCategoryForm, EditCategoryForm

# Create your views here.

def index(request):
    context = {
        
    }
    return render(request, "dashboard.html", context)

def categories(request):
    img_height = 100
    img_width = 100

    context = {
        'categories': Category.objects.all(),
        'img_height': img_height,
        'img_width': img_width
    }
    return render(request, "categories.html", context)

def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CreateCategoryForm()
        context = {
            'form': form,
        }
    return render(request, "create_category.html", context)

def edit_category(request, pk):
    instance = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = EditCategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = EditCategoryForm(instance=instance)
        context = {
            'form': form
        }
    return render(request, "edit_category.html", context)

def delete_category(request, pk):
    
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('categories')
        
    context = {
        'category': category
    }
    return render(request, "delete_category.html", context)

def category_products(request):
    pass