from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .models import *
from tramitesApp.models import Alumno
# Create your views here.
def acceder(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario,password=password)
            if usuario is not None:
                if usuario.groups.filter(name='GrupoSecretaria') or usuario.groups.filter(name='GrupoDirector'):
                    if usuario.groups.filter(name='GrupoSecretaria'):
                        login(request,usuario) 
                        return redirect("secre")
                    else:
                        login(request,usuario)
                        return redirect("direc")
                else:
                    login(request,usuario)
                    return redirect("home")
            else:
                messages.error(request,"Los datos son incorrectos")
        else:
            messages.error(request,"Los datos son incorrectos")

    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def homePage(request):
    context={}
    return render(request,"bienvenido.html",context)

def salir(request):
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login")

def registrar(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(username = form.cleaned_data['username'], 
                                                first_name = form.cleaned_data['nombres'],
                                                last_name = form.cleaned_data['apellidos'],
                                                email=form.cleaned_data['email'], 
                                                password=form.cleaned_data['password1'])
                group = Group.objects.get(name='GrupoAlumno')
                user.groups.add(group)
                user.save()                  
                alumno = Alumno()
                alumno.user = user
                alumno.nombres=form.cleaned_data['nombres']
                alumno.apellidos=form.cleaned_data['apellidos']
                alumno.codigo=form.cleaned_data['codigo']
                alumno.dni=form.cleaned_data['dni']
                alumno.direccion=form.cleaned_data['direccion']
                alumno.email=form.cleaned_data['email']
                alumno.telefono=form.cleaned_data['telefono']
                alumno.facultad=form.cleaned_data['facultad']
                alumno.escuela=form.cleaned_data['escuela']
                alumno.estado=True
                alumno.save()
                messages.success(request, 'Se registro correctamente')    
                return redirect("login")          
            except Exception as e:
                Alumno.objects.filter(id=alumno.id).delete()
                messages.error(request, "El usuario ya está registrado")
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, "registrar.html", context)