from .cart import Cart

def cart(request):
    """
    Context processor to make the cart accessible in all templates.
    """
    return {'cart': Cart(request)}
