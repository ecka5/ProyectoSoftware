from django.contrib import admin
from django.urls import path, include
from seguridadApp.views import acceder, homePage
from django.contrib.auth import views

urlpatterns = [
    path('', acceder, name = "login"),
    path('home/', homePage, name="home"),
#     path('logout/',salir,name="logout"),
]
