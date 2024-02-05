from product.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        
        if ('session_key' not in request.session):
            cart = self.session['session_key'] = {} #initializes blank session cart object
        
        self.cart = cart

    def add_item (self, added_product, prod_qty):
        product_id = str(added_product.product_id)
        product_quantity = str(prod_qty)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_quantity)

        self.session.modified = True