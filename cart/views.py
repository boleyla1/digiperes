from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .cart import Cart
from product.models import Product
from django.http import JsonResponse


def CartView(request):
    cart = Cart(request)
    cart_product = cart.GetProducts()
    quantitys = cart.get_quants()

    return render(request, 'cart/cart.html', {'cart': cart, 'cart_product': cart_product , 'quantitys': quantitys})


def Cartadd(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('Product_id'))
        Product_qty = str(request.POST.get('Product_qty'))

        product = get_object_or_404(Product, id=Product_id)
        cart.add(product=product, quantity=Product_qty)
        cart_quantity = cart.__len__()
        # response = JsonResponse({'product title': product.title})
        response = JsonResponse({"qty": cart_quantity})
        print(type(Product_id))
        return response

# Create your views here.
