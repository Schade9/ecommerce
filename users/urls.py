from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
]