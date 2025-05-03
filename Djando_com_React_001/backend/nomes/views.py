from django.shortcuts import render
from rest_framework import generics
from .models import Nome
from .serializers import NomeSerializer

class NomeListCreateView(generics.ListCreateAPIView):
    queryset = Nome.objects.all()
    serializer_class = NomeSerializer

