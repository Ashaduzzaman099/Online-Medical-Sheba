from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm


class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'user_name', 'phone_number', 'date_of_birth', 'role', 'gender']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        # Custom placeholders for each field
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Enter your full name'})
        self.fields['user_name'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Enter your phone number'})
        self.fields['date_of_birth'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise ValidationError("Passwords do not match.")

        # Validate password strength using Django's validators
        password_validation.validate_password(password=password)

        return cleaned_data
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        # Validate Bangladeshi phone number format
        if not phone_number.isdigit() or len(phone_number) != 11 or not phone_number.startswith('01'):
            raise ValidationError("Phone number must be 11 digits and start with '01'.")

        return phone_number

class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        max_length=255,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        required=True
    )



User = get_user_model()
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'date_of_birth', 'blood_group', 'gender']  # Include gender
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'})  # Dropdown widget for gender
        }

   #  def __init__(self, *args, **kwargs):
   #      super(ProfileUpdateForm, self).__init__(*args, **kwargs)
   #      self.fields['full_name'].required = True
   #      self.fields['phone_number'].required = True
   #      self.fields['date_of_birth'].required = True
   #      self.fields['blood_group'].required = True
   #      self.fields['gender'].required = True

    def clean(self):
        cleaned_data = super().clean()
        
        # Check for required fields
        if not cleaned_data.get('full_name'):
            self.add_error('full_name', "Full name is required.")
        
        if not cleaned_data.get('phone_number'):
            self.add_error('phone_number', "Phone number is required.")

        if not cleaned_data.get('date_of_birth'):
            self.add_error('date_of_birth', "Date of birth is required.")

        if not cleaned_data.get('blood_group'):
            self.add_error('blood_group', "Blood group is required.")

        if not cleaned_data.get('gender'):
            self.add_error('gender', "Gender is required.")

    def clean_phone_number(self):
         phone_number = self.cleaned_data.get('phone_number')

         # Validate Bangladeshi phone number format
         if not phone_number.isdigit() or len(phone_number) != 11 or not phone_number.startswith('01'):
               raise ValidationError("Phone number must be 11 digits and start with '01'.")

         return phone_number


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders to each field
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter old password',
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter new password',
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm new password',
        })