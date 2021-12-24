from django import forms
from easyBuy.models import Category

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'image']

class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'image']