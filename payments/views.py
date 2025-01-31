from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ShippingForm
from .models import ShippingAddress, OrderItem, Order
from django.http import JsonResponse
from cart.cart import Cart


@login_required
def checkout_view(request):
    
    cart = Cart(request)
    cart_products = cart.get_prods()  
    quantities = cart.get_quants()   
    totals = cart.cart_total()

    for product in cart_products:
        # Ensure quantity is an integer
        quantity = int(quantities.get(str(product.id), 0))  # Default to 0 if not found
        
        # Calculate subtotal for the product
        product.sub_total = product.price * quantity

    # Fetch the existing shipping address for the user
    shipping_address = ShippingAddress.objects.filter(user=request.user).first()

    if request.method == 'POST':
        # Bind the form to POST data and existing instance
        form = ShippingForm(request.POST, instance=shipping_address)

        if form.is_valid():
            # Save the form and associate with the user
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user
            shipping_address.save()
            messages.success(request, "Shipping details saved successfully!")

            context = {
               'cart': cart,
               'cart_products': cart_products,
               'quantities': quantities,
               'totals': totals,
               'shipping_info': form,
            }

            return render(request, 'payments/billing_info.html', context)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # Prefill the form with existing data or leave it blank
        if shipping_address:
            form = ShippingForm(instance=shipping_address)
        else:
            form = ShippingForm()  # Blank form for new user

    context = {
        'shipping_form': form,
    }
    return render(request, 'payments/checkout.html', context)


def validate_shipping_form(request):
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request'})



def billing_info(request):
    
    return render(request, 'payments/payment.html')


@login_required
def payment_view(request):
    # Retrieve cart details
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()  # Total price from cart

    for product in cart_products:
        # Ensure quantity is an integer
        quantity = int(quantities.get(str(product.id), 0))
        # Calculate subtotal for the product
        product.sub_total = product.price * quantity

    shipping_address = ShippingAddress.objects.filter(user=request.user).first()

    context = {
        'cart': cart,
        'cart_products': cart_products,
        'quantities': quantities,
        'totals': totals,
        'shipping_address': shipping_address,
    }

    return render(request, 'payments/payment.html', context)


@login_required
def handle_payment_success(request):
    """
    Handle order placement after a successful PayPal payment.
    """
    if request.method == 'POST':
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.cart_total()

        shipping_address = ShippingAddress.objects.filter(user=request.user).first()

        # Create the order
        order = Order.objects.create(
            user=request.user,
            full_name=shipping_address.shipping_full_name,
            email=shipping_address.shipping_email,
            shipping_address=f"{shipping_address.shipping_address1}, {shipping_address.shipping_address2}, {shipping_address.shipping_city}, {shipping_address.shipping_state}, {shipping_address.shipping_country}, {shipping_address.shipping_zip_code}",
            amount_paid=totals,
        )

        # Create order items
        for product in cart_products:
            quantity = int(quantities.get(str(product.id), 0))
            OrderItem.objects.create(
                order=order,
                product=product,
                user=request.user,
                quantity=quantity,
                price=product.price,
            )

        # Clear the cart after placing the order
        cart.clear()

        return JsonResponse({'success': True, 'order_id': order.id})

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)



    




def payment_success(request):
    return render(request, 'payments/payment_success.html')

