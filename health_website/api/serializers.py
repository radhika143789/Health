from rest_framework import serializers
from .models import MentalHealthData

class MentalHealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthData
        fields = '__all__'
