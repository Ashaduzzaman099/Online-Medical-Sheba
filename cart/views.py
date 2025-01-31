from django.shortcuts import render, get_object_or_404
from .cart import Cart
from medicine_store.models import Medicine
from django.http import JsonResponse
from django.contrib import messages

def cart_detail(request):
    """
    Display the cart details with calculated subtotals.
    """
    cart = Cart(request)
    cart_products = cart.get_prods()  # Get products in the cart
    quantities = cart.get_quants()   # Get quantities from the cart
    totals = cart.cart_total()
    
    # Attach subtotals to products
    for product in cart_products:
        # Ensure quantity is an integer
        quantity = int(quantities.get(str(product.id), 0))  # Default to 0 if not found
        
        # Calculate subtotal for the product
        product.sub_total = product.price * quantity

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'cart_products': cart_products,
        'quantities': quantities,
        'totals': totals,
    })

def cart_add(request):
    """
    Add a product to the cart via AJAX.
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Medicine, id=product_id)

        cart.add(product=product, quantity=quantity)

        response = JsonResponse({'quantity': cart.__len__()})
        return response





def cart_update(request):
    """
    Update product quantity in the cart via AJAX.
    """
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))
        
        # Get the product
        product = get_object_or_404(Medicine, id=product_id)
        
        # Update the cart
        cart.update(product=product, quantity=quantity)

        return JsonResponse({'success': True, 'quantity': quantity})
    
def cart_remove(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
		cart.delete(product_id=product_id)

		response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response