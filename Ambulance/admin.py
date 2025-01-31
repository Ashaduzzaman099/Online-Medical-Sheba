from django.contrib import admin
from .models import Ambulance

@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'type', 
        'status', 
        'location', 
        'latitude', 
        'longitude', 
        'contact_number', 
        'user_rating'
    )
    list_filter = ('type', 'status', 'location')  # Filters for type, status, and location
    search_fields = ('name', 'location', 'contact_number')  # Searchable fields
