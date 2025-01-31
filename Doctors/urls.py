from django.urls import path
from . import views

app_name="Doctors"

urlpatterns = [
    path('add-doctor-profile/', views.add_doctor_profile, name='add_doctor_profile'),
    path('doctor-profile/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),
    path('book-appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('success/', views.success_view, name='success_view'),
    path('show/',views.doctor_list, name="doctor_list"),
    path('payment/', views.payment_view, name='payment_view'),
    path('manage-appointments/', views.manage_appointments, name='manage_appointments'),
    path('update-appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('delete-appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('writePrecription', views.create_prescription_view, name='writePrecription'),


    
]
