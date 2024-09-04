from product.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product,quantity):
        Product_id = int(product.id)
        Product_qty = str(quantity)

        if Product_id in self.cart:
            pass
        else:
            self.cart[Product_id] = str(Product_qty)
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def GetProducts(self):
        product_ids = self.cart.keys()
        product = Product.objects.filter(id__in=product_ids)
        return product

    def get_quants(self):
        quantities = self.cart
        return quantities

