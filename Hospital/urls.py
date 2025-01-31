from django.urls import path
from . import views

app_name = 'Hospital'

urlpatterns = [
    path('findHospital/', views.findHospital, name='findHospital'),
]