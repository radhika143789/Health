from django.db import models

class MentalHealthData(models.Model):
    data_point = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.data_point

