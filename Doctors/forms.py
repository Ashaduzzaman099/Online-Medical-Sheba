from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    price = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Appointment
        fields = ['hospital', 'consultation_type', 'appointment_type', 'appointment_date', 'time_slot', 'price']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        """Ensure price is set for new patients."""
        cleaned_data = super().clean()
        appointment_type = cleaned_data.get('appointment_type')

        # Dynamically set price based on appointment type
        price_mapping = {
            'new_patient': 5,
            'follow_up': 2,
            'report_show': 0,
        }
        cleaned_data['price'] = price_mapping.get(appointment_type, 0)
        return cleaned_data
