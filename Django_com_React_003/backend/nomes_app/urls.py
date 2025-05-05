from django.urls import path
from .views import ListaNomes

urlpatterns = [
    path('nomes/', ListaNomes.as_view(), name='nomes-lista-criar'),
]
