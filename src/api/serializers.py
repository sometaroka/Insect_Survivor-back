from rest_framework import serializers
from .models import TestData 

class TestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestData
        fields = '__all__'
# Compare this snippet from src/api/serializers.py:
