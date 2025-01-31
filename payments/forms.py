from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
   shipping_full_name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=True)
   shipping_email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email Address'}), required=True)
   shipping_phone_number = forms.CharField(label="Phone Number", widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}), required=True)
   shipping_address1 = forms.CharField(label="Address1", widget=forms.TextInput(attrs={'placeholder': 'Address1'}), required=True)
   shipping_address2 = forms.CharField(label="Address2", widget=forms.TextInput(attrs={'placeholder': 'Address2'}), required=False)
   shipping_city = forms.CharField(label="City", widget=forms.TextInput(attrs={'placeholder': 'Put City'}), required=True)
   shipping_state = forms.CharField(label="State", widget=forms.TextInput(attrs={'placeholder': 'Put State'}), required=False)
   shipping_zip_code = forms.CharField(label="ZipCode", widget=forms.TextInput(attrs={'placeholder': 'Put Zipcode'}), required=False)
   shipping_country = forms.CharField(label="Country", widget=forms.TextInput(attrs={'placeholder': 'Put Country'}), required=True)


   class Meta:
      model = ShippingAddress
      fields = ('shipping_full_name', 'shipping_email', 'shipping_phone_number', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zip_code', 'shipping_country',)

      exclude = ['user',]



