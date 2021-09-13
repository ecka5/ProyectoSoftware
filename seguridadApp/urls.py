from django.contrib import admin
from django.urls import path, include
from seguridadApp.views import acceder, homePage,salir, registrar
from tramitesApp.views import secre,direc
from django.contrib.auth import views

urlpatterns = [
    path('', acceder, name = "login"),
    path('home/', homePage, name="home"),
    path('logout/',salir,name="logout"),
    path('registrar/',registrar,name="registrar"),
    path('secre/',secre,name="secre"),
    path('direc/',direc,name="direc"),
]
