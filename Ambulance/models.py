from django.db import models

class Ambulance(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('AC', 'AC'),
        ('Non-AC', 'Non-AC'),
        ('ALS', 'ALS'),
        ('ACLS', 'ACLS'),
        ('AIR', 'AIR'),
        ('ICU', 'ICU'),
        ('NICU', 'NICU'),
        ('Freezing', 'Freezing'),
    ]

    name = models.CharField(max_length=200)  # Ambulance service name
    type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)  # Type of service
    status = models.BooleanField(default=True)  # Availability status
    location = models.CharField(max_length=255)  # Service location
    latitude = models.FloatField()  # Latitude for map
    longitude = models.FloatField()  # Longitude for map
    contact_number = models.CharField(max_length=15)  # Contact information
    facilities = models.TextField()  # Facilities provided
    image_url = models.URLField(default="")  # Image of the ambulance
    user_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # User rating (e.g., 4.5)

    def __str__(self):
        return self.name

    def get_google_maps_url(self):
        return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
