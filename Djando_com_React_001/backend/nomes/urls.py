from django.urls import path
from .views import NomeListCreateView

urlpatterns = [
    path('nomes/', NomeListCreateView.as_view()),
]
