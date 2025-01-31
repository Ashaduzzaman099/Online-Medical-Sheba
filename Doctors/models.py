from django.db import models
from accounts.models import User

class DoctorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    about = models.TextField()
    hospital = models.CharField(max_length=255)
    specialties = models.CharField(max_length=255)
    experience = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    

    def __str__(self):
        return self.title
class Education(models.Model):
    doctor = models.ForeignKey(DoctorProfile, related_name='education', on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    result = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.degree_name} - {self.institution_name}"
class Availability(models.Model):
    doctor = models.ForeignKey(DoctorProfile, related_name='availability', on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    am_pm = models.CharField(max_length=2)
    available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day} ({self.start_time} - {self.end_time})"
    


class Appointment(models.Model):
    APPOINTMENT_TYPES = [
        ('new_patient', 'New Patient'),
        ('follow_up', 'Follow Up'),
        ('report_show', 'Report Show'),
    ]
    CONSULTATION_TYPES = [
        ('face_to_face', 'Face to Face'),
        ('online', 'Online'),
    ]

    doctor = models.ForeignKey('DoctorProfile', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.CharField(max_length=255)
    consultation_type = models.CharField(max_length=20, choices=CONSULTATION_TYPES)
    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPES)
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_appointment_amount(self):
        """Determine the amount based on the appointment type."""
        amount_mapping = {
            'new_patient': 5,  # $5
            'follow_up': 2,    # $2
            'report_show': 0,  # $0
        }
        return amount_mapping.get(self.appointment_type, 0)  # Default to $0 if type not found

    def __str__(self):
        return f"Appointment with {self.doctor.title} on {self.appointment_date} ({self.time_slot})"
    


from django.db import models
from accounts.models import User

class BookingRequest(models.Model):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CANCELED = 'Canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled'),
    ]

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.CharField(max_length=255)
    consultation_type = models.CharField(max_length=255)
    appointment_type = models.CharField(max_length=255)
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.patient.full_name} - {self.appointment_date}'

    class Meta:
        ordering = ['-appointment_date']



class Prescription(models.Model):
    doctor = models.ForeignKey('DoctorProfile', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, null=True)
    doctor_comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.username} by {self.doctor.user.username}"

class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='medicines')
    name = models.CharField(max_length=255)
    breakfast_dosage = models.BooleanField(default=False)  # Dosage at breakfast
    lunch_dosage = models.BooleanField(default=False)  # Dosage at lunch
    dinner_dosage = models.BooleanField(default=False)  # Dosage at dinner
    meal_remark = models.CharField(max_length=10, choices=[('before', 'Before Meal'), ('after', 'After Meal')], null=True, blank=True)
    additional_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} for {self.prescription.patient.username}"

