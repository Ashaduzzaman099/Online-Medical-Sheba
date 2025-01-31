from django.contrib import admin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'doctor_count', 'specialty_count', 'fee_range')
