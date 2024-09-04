from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView, name='cart'),
    path('add/', views.Cartadd, name='cartadd'),
]