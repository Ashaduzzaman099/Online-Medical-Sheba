from django.shortcuts import render
from .models import Ambulance

# Create your views here.


def findAmbulance(request):
   ambulances = Ambulance.objects.all()
   return render(request, 'Ambulance/findAmbulance.html', {'ambulances': ambulances})
