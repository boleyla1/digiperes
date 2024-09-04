from django.shortcuts import render, redirect, reverse
from .models import UserManager, Otp, User
from .forms import loginform, registerform, CheckOtpForm
from django.contrib.auth import authenticate, login, logout
import ghasedakpack
from random import randint
from django.utils.crypto import get_random_string
from uuid import uuid4

SMS = ghasedakpack.Ghasedak('a7936a8d941e397fe9aaa276b07e5e18608ce3fda0134d7f2ea976725f773d64ebjgvm8mtRYkkrWC')


def Users(request):
    user = UserManager.objects.all()
    phone = Otp.objects.all()
    return render(request, 'pages/index.html', {'user': user}, {'phone': phone})


def UserLogin(request):
    form = loginform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cleaneddata = form.cleaned_data
            user = authenticate(username=cleaneddata['phone'], password=cleaneddata['password'])
            print(user)
            if user is not None:
                login(request, user)
                form.add_error('phone', 'یا موفقیت وارد شدید')
                return redirect('/')
            else:
                form.add_error('phone', 'شماره تلفن درست نیست')
        else:
            form.add_error('phone', 'به درستی وارد نشد')

        # form = loginform()
    return render(request, 'account/login.html', {'form': form})


def UserLogout(request):
    logout(request)
    return redirect('/')


def UserRegister(request):
    form = registerform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            randcode = randint(10000, 99999)
            cleaneddata = form.cleaned_data
            SMS.verification(
                {'receptor': cleaneddata["phone"], 'type': '1', 'template': 'digiboleyla', 'param1': randcode})
            token = str(uuid4())
            Otp.objects.create(phone=cleaneddata["phone"], code=randcode, token=token)
            print(randcode)
            return redirect(reverse('CheckOtp') + f"?token={token}")
        else:
            form.add_error('phone', 'به درستی وارد نشد')
    return render(request, 'account/register.html', {'form': form})


def CheckOtp(request):
    token = request.GET.get('token')
    phone = request.GET.get('phone')
    form = CheckOtpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cleaneddata = form.cleaned_data
            if Otp.objects.filter(code=cleaneddata['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user = User.objects.create_user(phone=otp.phone)
                login(request, user)
                return redirect('/')
        else:
            form.add_error('phone', 'به درستی وارد نشد')
    return render(request, 'account/verify-phone-number.html', {'form': form})


def nav(request):
    user = UserManager.objects.all()
    phone = Otp.objects.all()
    return render(request, 'pages/navbar.html', {'user': user, 'phone': phone})
# Create your views here.
