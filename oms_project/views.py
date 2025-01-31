from django.http import response
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from medicine_store.models import Medicine
from Hospital.models import Hospital
from Ambulance.models import Ambulance
from django.urls import reverse


def home(request):
    # Fetch top-selling medicines (top 4)
    top_selling_medicines = Medicine.objects.filter(is_top_selling=True)[:4]
    
    # Fetch top hospitals (top 4)
    top_hospitals = Hospital.objects.all()[:4]  # You can adjust the filter as needed
    
    # Fetch top ambulances (top 4)
    top_ambulances = Ambulance.objects.all()[:4]  # You can adjust the filter as needed
    
    # Context to pass to the template
    context = {
        'top_selling_medicines': top_selling_medicines,
        'top_hospitals': top_hospitals,
        'top_ambulances': top_ambulances,  # Add the top_ambulances to context
    }
    
    return render(request, 'index.html', context)


