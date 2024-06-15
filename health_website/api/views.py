from rest_framework import viewsets
from .models import MentalHealthData
from .serializers import MentalHealthDataSerializer

class MentalHealthDataViewSet(viewsets.ModelViewSet):
    queryset = MentalHealthData.objects.all()
    serializer_class = MentalHealthDataSerializer

