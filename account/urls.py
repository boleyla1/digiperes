from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('register/', views.UserRegister, name='register'),
    path('checkotp/', views.CheckOtp, name='CheckOtp'),
]