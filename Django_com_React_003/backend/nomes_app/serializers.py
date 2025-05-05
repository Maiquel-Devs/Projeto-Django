from rest_framework import serializers
from .models import Nome

# Transforma Json em Python e depois volta para o models.py
class NomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nome
        fields = '__all__'