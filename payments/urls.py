from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('validate-shipping-form/', views.validate_shipping_form, name='validate_shipping_form'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('billing_info/', views.billing_info, name='billing_info'),
    path('pay/', views.payment_view, name='payment_view'),  # Payment view with PayPal button
    path('handle-payment-success/', views.handle_payment_success, name='handle_payment_success'),  # Handle PayPal success
]

