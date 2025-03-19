from django.contrib.auth import views as auth_views  
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),  
    path('login/', auth_views.LoginView.as_view(template_name='Cadastro/login.html', next_page='/home/'), name='login'),  
    path('home/', views.home, name='home'),  
]
