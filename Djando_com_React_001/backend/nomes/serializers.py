from rest_framework import serializers
from .models import Nome

class NomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nome
        fields = '__all__'
