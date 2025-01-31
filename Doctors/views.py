from django.shortcuts import render, redirect, get_object_or_404
from .models import DoctorProfile, Education, Availability
from Hospital.models import Hospital
from accounts.models import User

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import DoctorProfile, Appointment, PrescriptionMedicine, Prescription
from datetime import date

@login_required
def create_prescription_view(request):
    doctor = request.user
    appointments = Appointment.objects.filter(doctor__user=doctor).select_related('patient')
    patients = User.objects.filter(id__in=appointments.values_list('patient__id', flat=True))

    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_comment = request.POST.get('doctor_comment')
        patient = User.objects.get(id=patient_id)
        appointment = appointments.filter(patient=patient).first()

        date_of_birth = patient.date_of_birth
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        else:
            age = None  # Handle cases where date_of_birth is not available

        # Create Prescription
        prescription = Prescription.objects.create(
            doctor=appointment.doctor,
            patient=patient,
            appointment=appointment,
            age=age,
            sex=patient.gender,  # Assuming profile model with `gender`
            doctor_comment=doctor_comment,
        )

        # Add Medicines to Prescription
        medicine_count = int(request.POST.get('medicine_count', 0))
        for i in range(1, medicine_count + 1):
            name = request.POST.get(f'medicine_name_{i}')
            breakfast_dosage = request.POST.get(f'breakfast_dosage_{i}') == 'on'
            lunch_dosage = request.POST.get(f'lunch_dosage_{i}') == 'on'
            dinner_dosage = request.POST.get(f'dinner_dosage_{i}') == 'on'
            meal_remark = request.POST.get(f'meal_remark_{i}')
            additional_notes = request.POST.get(f'additional_notes_{i}')

            if name:
                PrescriptionMedicine.objects.create(
                    prescription=prescription,
                    name=name,
                    breakfast_dosage=breakfast_dosage,
                    lunch_dosage=lunch_dosage,
                    dinner_dosage=dinner_dosage,
                    meal_remark=meal_remark,
                    additional_notes=additional_notes,
                )

        return render(request, 'Doctors/success.html')  # Redirect to success page

    context = {
        'appointments': appointments,
        'patients': patients,
    }
    return render(request, 'Doctors/write_prescription.html', context)




def add_doctor_profile(request):
    if request.method == "POST":
        # DoctorProfile data
        user_id = request.POST.get('user_id')
        title = request.POST.get('title')
        about = request.POST.get('about')
        hospital_id = request.POST.get('hospital')
        specialties = request.POST.get('specialties')
        experience = request.POST.get('experience')
        license_number = request.POST.get('license_number')
        address = request.POST.get('address')

        # Fetch the User instance by ID
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return render(request, 'Doctors/Doctor_info.html', {
                'error': 'User does not exist.',
                'hospital_list': Hospital.objects.all(),
            })

        # Fetch the hospital instance
        try:
            hospital = Hospital.objects.get(id=hospital_id)
        except Hospital.DoesNotExist:
            return render(request, 'Doctors/Doctor_info.html', {
                'error': 'Selected hospital does not exist.',
                'hospital_list': Hospital.objects.all(),
            })

        # Save DoctorProfile
        doctor = DoctorProfile.objects.create(
            user=user,  # Assign the actual User instance
            title=title,
            about=about,
            hospital=hospital,
            specialties=specialties,
            experience=experience,
            license_number=license_number,
            address=address
        )

        # Education data
        institution_names = request.POST.getlist('institution_name[]')
        degree_names = request.POST.getlist('degree_name[]')
        results = request.POST.getlist('result[]')

        for institution, degree, result in zip(institution_names, degree_names, results):
            Education.objects.create(
                doctor=doctor,
                institution_name=institution,
                degree_name=degree,
                result=result
            )

        # Availability data
        days = request.POST.getlist('availability_day[]')
        from_times = request.POST.getlist('availability_from[]')
        to_times = request.POST.getlist('availability_to[]')
        am_pm_values = request.POST.getlist('availability_ampm[]')
        availabilities = request.POST.getlist('availability_available[]')

        for day, from_time, to_time, am_pm, available in zip(days, from_times, to_times, am_pm_values, availabilities):
            Availability.objects.create(
                doctor=doctor,
                day=day,
                start_time=from_time,
                end_time=to_time,
                am_pm=am_pm,
                available=(available == 'on')
            )

        return redirect('Doctors:success_view')  # Redirects to success page

    # Fetch the list of hospitals for the form dropdown
    hospital_list = Hospital.objects.all()
    return render(request, 'Doctors/Doctor_info.html', {'hospital_list': hospital_list})
# Success Page
def success_view(request):
    return render(request, 'Doctors/success.html')

# List of all Doctors
def doctor_list(request):
    # Fetch all DoctorProfile records
    doctor_profiles = DoctorProfile.objects.all()

    # Prepare a list to hold the combined doctor details
    doctor_details = []

    for doctor in doctor_profiles:
        # Fetch education and availability details for the doctor
        education_details = Education.objects.filter(doctor=doctor)
        availability_details = Availability.objects.filter(doctor=doctor)

        # Append the combined data for each doctor
        doctor_details.append({
            'doctor': doctor,
            'user': doctor.user,  # Accessing the User instance directly through FK
            'education': education_details,
            'availability': availability_details,
        })

    return render(request, 'Doctors/doctor_list.html', {'doctor_details': doctor_details})



from django.http import HttpResponseRedirect
from django.urls import reverse

def doctor_profile(request, doctor_id=None):
    if not doctor_id:
        # Redirect to a default page or display an error message
        return HttpResponseRedirect(reverse('doctor_list'))  # Redirect to the doctor list view

    # Fetch the specific doctor by ID
    doctor = get_object_or_404(DoctorProfile, id=doctor_id)
    
    # Fetch related data
    education_details = Education.objects.filter(doctor=doctor)
    availability_details = Availability.objects.filter(doctor=doctor)
    
    context = {
        'doctor': doctor,
        'education_details': education_details,
        'availability_details': availability_details,
    }
    
    return render(request, 'Doctors/Doctor_Profile.html', context)



@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(DoctorProfile, id=doctor_id)
    availability_details = doctor.availability.all()

    # Define price mapping for appointment types
    price_mapping = {
        'new_patient': 5,
        'follow_up': 2,
        'report_show': 0,
    }

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Access cleaned data
            hospital = form.cleaned_data['hospital']
            consultation_type = form.cleaned_data['consultation_type']
            appointment_type = form.cleaned_data['appointment_type']
            appointment_date = form.cleaned_data['appointment_date']
            time_slot = form.cleaned_data['time_slot']

            # Check if the patient already has an appointment with this doctor
            existing_appointment = Appointment.objects.filter(
                patient=request.user,  # Assuming the user is the patient
                doctor=doctor,
                appointment_date=appointment_date,
                time_slot=time_slot
            ).exists()

            if existing_appointment:
                messages.error(request, "You already have an appointment with this doctor at the specified time.")
                return redirect('Doctors:book_appointment', doctor_id=doctor.id)

            # Determine price based on appointment type
            price = price_mapping.get(appointment_type, 0)

            # Save appointment data in the session
            request.session['appointment_data'] = {
                'doctor_id': doctor.id,
                'hospital': hospital,
                'consultation_type': consultation_type,
                'appointment_type': appointment_type,
                'appointment_date': appointment_date.strftime('%Y-%m-%d'),
                'time_slot': time_slot,
                'price': price
            }

            return redirect('Doctors:payment_view')  # Redirect to payment page
    else:
        form = AppointmentForm()

    return render(request, 'Doctors/book_appointment.html', {
        'form': form,
        'doctor': doctor,
        'availability_details': availability_details,
    })


@login_required
def payment_view(request):
    appointment_data = request.session.get('appointment_data', None)
    if not appointment_data:
        messages.error(request, "No appointment data found. Please book again.")
        return redirect('Doctors:doctor_profile', doctor_id=appointment_data['doctor_id'])

    if request.method == 'POST':
        # Simulate payment process here
        payment_successful = True  # Integrate a payment gateway like Stripe/PayPal here

        if payment_successful:
            # Save the appointment if payment is successful
            doctor = get_object_or_404(DoctorProfile, id=appointment_data['doctor_id'])
            appointment = Appointment(
                doctor=doctor,
                patient=request.user,
                hospital=appointment_data['hospital'],
                consultation_type=appointment_data['consultation_type'],
                appointment_type=appointment_data['appointment_type'],
                appointment_date=appointment_data['appointment_date'],
                time_slot=appointment_data['time_slot']
            )
            appointment.save()

            messages.success(request, "Appointment booked successfully!")
            return redirect('Doctors:success_view')
        else:
            messages.error(request, "Payment failed. Please try again.")
            return redirect('Doctors:payment_view')

    return render(request, 'Doctors/payment.html', {
        'appointment_data': appointment_data,
    })

from .models import DoctorProfile, BookingRequest



from .models import Appointment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Appointment, DoctorProfile

@login_required
def manage_appointments(request):
    """
    View for doctors to manage their appointments.
    Only fetch appointments related to the logged-in doctor.
    """
    # Check if the user is a doctor
    if request.user.role == 'doctor':
        try:
            # Get the DoctorProfile instance for the logged-in user
            doctor_profile = DoctorProfile.objects.get(user=request.user)

            # Filter appointments where the doctor matches the doctor_profile
            appointments = Appointment.objects.filter(doctor=doctor_profile)
        except DoctorProfile.DoesNotExist:
            # Handle the case where the doctor profile does not exist
            appointments = []
    else:
        # Redirect other users
        appointments = []

    context = {'appointments': appointments}
    return render(request, 'Doctors/manage_appointment.html', context)

 
    

@login_required
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('Doctors:manage_appointments')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'Doctors/update_appointment.html', {'form': form})

@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('Doctors:manage_appointments')

    return render(request, 'Doctors/confirm_delete.html', {'appointment': appointment})



