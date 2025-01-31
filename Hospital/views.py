# appointments/views.py
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from .models import Hospital
from django.db.models import Q


def findHospital(request):
    query = request.GET.get('query', '')  # Optional: Filter hospitals by query
    if query:
        hospitals = Hospital.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query)
        )
    else:
        hospitals = Hospital.objects.all()

    # Prepare data for the template
    hospital_list = [
        {
            "name": hospital.name,
            "address": hospital.address,
            "latitude": hospital.latitude,
            "longitude": hospital.longitude,
            "logo_url": hospital.logo_url,
            "doctor_count": hospital.doctor_count,
            "specialty_count": hospital.specialty_count,
            "fee_range": hospital.fee_range,
        }
        for hospital in hospitals
    ]

    context = {"hospital_list": hospital_list}
    return render(request, "Hospital/findHospital.html", context)
