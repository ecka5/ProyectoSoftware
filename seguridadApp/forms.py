from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    nombres = forms.CharField(max_length=40)
    apellidos=forms.CharField(max_length=40)
    codigo=forms.CharField(label='Código de estudiante', max_length=10)   
    dni=forms.CharField(label='DNI',max_length=8)
    direccion=forms.CharField(max_length=80)
    email=forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    telefono=forms.CharField(max_length=9)
    facultad=forms.CharField(max_length=10, initial="INGENIERIA")
    escuela=forms.CharField(max_length=22, initial="INGENIERIA DE SISTEMAS")
    estado=forms.BooleanField(initial=True)