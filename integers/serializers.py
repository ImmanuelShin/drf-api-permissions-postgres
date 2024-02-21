from rest_framework import serializers
from .models import Integer

class IntegerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integer
        fields = '__all__'