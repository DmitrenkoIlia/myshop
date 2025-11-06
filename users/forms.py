from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        
        labels = {
            'email': "Електронна пошта",
            'first_name': "Ім'я",
            'last_name': 'Прізвище',
        }

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше ім'я"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше прізвище'}),
        }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'city', 'street', 'house', 'flat']

        labels = {
            'phone': 'Телефон',
            'city': 'Місто',
            'street': 'Вулиця',
            'house': 'Будинок',
            'flat': 'Квартира',
        }
        
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+380 (XX) XXX-XX-XX'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Напр., Київ'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Напр., Хрещатик'}),
            'house': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Напр., 26'}),
            'flat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Напр., 10'}),
        }