from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import models
from django.core import validators


class loginform(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg '
                                               'focus:outline-none focus:ring-2 '
                                               'focus:ring-red-500',
                                      'placeholder': 'شماره تلفن'}))
    password = forms.CharField(max_length=12,
                               widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg '
                                                                          'focus:outline-none focus:ring-2 '
                                                                          'focus:ring-red-500',
                                                                 'placeholder': 'پسورد'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) > 12:
            raise ValidationError('تعداد تلفن وارد شده معتبر نیست', code='invalid_phone', params={'value': f'{phone}'})
        return phone


class registerform(forms.Form):
    phone = forms.CharField(validators=[validators.MaxLengthValidator(11)],
                            widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg '
                                                                   'focus:outline-none focus:ring-2 '
                                                                   'focus:ring-red-500',
                                                          'placeholder': 'شماره تلفن'}))


class CheckOtpForm(forms.Form):
    code = forms.CharField(max_length=5,widget=forms.TextInput(attrs={'class': 'form-control'}),
                           validators=[validators.MaxLengthValidator(5)])

