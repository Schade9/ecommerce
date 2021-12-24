from django.urls import path
from staff import views

urlpatterns = [
    path('', views.index, name="staff_index"),
    path('categories/', views.categories, name="categories"),
    path('create_category', views.create_category, name="create_category"),
    path('edit_category/<int:pk>/', views.edit_category, name="edit_category"),
    path('<int:pk>/delete_category', views.delete_category, name="delete_category"),
    # path('store/', views.store, name="store"),
]