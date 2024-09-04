from django.shortcuts import render
from .models import Product
from . import models


# Create your views here.


def ProductView(request, pk):
    products = models.Product.objects.all()
    product = models.Product.objects.get(id=pk)
    return render(request, 'product/single-product.html', {'products': products, 'product': product})
