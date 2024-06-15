from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MentalHealthDataViewSet

router = DefaultRouter()
router.register(r'mentalhealthdata', MentalHealthDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
