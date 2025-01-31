# hospital/models.py
from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    logo_url = models.URLField()
    doctor_count = models.IntegerField()
    specialty_count = models.IntegerField()
    fee_range = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_google_maps_url(self):
        return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
