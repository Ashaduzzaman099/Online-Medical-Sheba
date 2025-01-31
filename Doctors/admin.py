from django.contrib import admin

# Register your models here.
# Doctors/admin.py

from .models import DoctorProfile, Education, Availability, Appointment

admin.site.register(DoctorProfile)
admin.site.register(Education)
admin.site.register(Availability)
admin.site.register(Appointment)
