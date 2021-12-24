from django.urls import path
from easyBuy import views

urlpatterns = [
    path('', views.index, name="index"),
    path('productdetail/<int:pk>/', views.product_detail, name="product_detail"),
    path('categoryproducts/<int:pk>/', views.category_products, name="category_products"),
    path('store/', views.store, name="store"),
]