from rest_framework import generics
from .models import Nome
from .serializers import NomeSerializer


# Manda os dados recebidos em JSON para o arquivo serializers.py 
class ListaNomes(generics.ListCreateAPIView):
    queryset = Nome.objects.all()
    serializer_class = NomeSerializer