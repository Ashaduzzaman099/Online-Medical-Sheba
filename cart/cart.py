from medicine_store.models import Medicine

class Cart:
    def __init__(self, request):
        """
        Initialize the cart object.
        The cart data is stored in the session using a key named 'session_key'.
        """
        self.session = request.session
        self.cart = self.session.get('cart', {})
        self.request = request
        self.session = request.session

        cart = self.session.get('session_key')

        # If the cart doesn't exist in the session, create an empty cart
        if not cart:
            cart = self.session['session_key'] = {}
        
        self.cart = cart

    def add(self, product, quantity=1):
        """
        Add a product to the cart or update its quantity.
        :param product: The product to add or update.
        :param quantity: The quantity to add.
        """
        product_id = str(product.id)  # Convert to string for JSON compatibility
        product_qty = str(quantity)

        if product_id in self.cart:
            # Update the quantity if the product is already in the cart
            self.cart[product_id]['quantity'] += quantity
        else:
            # Add a new product with both price and quantity in a single update
            self.cart[product_id] = int(product_qty)

        self.save()

    def __len__(self):
        return len(self.cart)
    

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # use ids to get products from database
        products = Medicine.objects.filter(id__in=product_ids)
        return products
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def sub_total(self):
        # Calculate subtotal for each product
        product_ids = self.cart.keys()
        products = Medicine.objects.filter(id__in=product_ids)
        subtotals = {
            str(product.id): product.price * int(self.cart[str(product.id)])
            for product in products
        }
        return subtotals
    
    def cart_total(self):
      # Retrieve product IDs and their quantities
      product_ids = self.cart.keys()
      quantities = self.cart

      # Fetch products that match the IDs
      products = Medicine.objects.filter(id__in=product_ids)

      # Calculate total using a generator expression
      total = sum(
         product.price * quantities[str(product.id)]
         if product else product.price * quantities[str(product.id)]
         for product in products
      )

      return total

    
    def update(self,product,quantity):
        product_id = int(product.id)
        product_qty = int(quantity)

        ourcart = self.cart

        ourcart[product_id] = product_qty

        self.session.modified = True
        thing = self.cart
        return thing
    
    def delete(self, product_id):
      # Delete from dictionary/cart
      product_id = str(product_id)
      cart = self.cart
      if product_id in self.cart:
         del self.cart[product_id]

      self.session.modified = True

      # Deal with logged in user
      if self.request.user.is_authenticated:
         current_user = Medicine.objects.filter(user__id=self.request.user.id)
         carty = str(self.cart).replace("'", "\"")
         current_user.update(old_cart=carty)




    def save(self):
        """
        Mark the session as modified to ensure it gets saved.
        """
        self.session.modified = True

    def remove(self, product_id):
        """
        Remove a product from the cart.
        :param product_id: The ID of the product to remove.
        """
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """
        Clear the cart.
        """
        self.session['session_key'] = {}
        self.save()

    def __iter__(self):
        """
        Iterate through the cart items.
        Can be used in templates or views.
        """
        for product_id, details in self.cart.items():
            yield {
                'product_id': product_id,
                'quantity': details['quantity']
            }

   #  def __len__(self):
   #      """
   #      Count the number of items in the cart.
   #      """
   #      return sum(item['quantity'] for item in self.cart.values())
