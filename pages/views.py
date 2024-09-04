from django.shortcuts import render
from product.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products': products})
# Create your views here.
