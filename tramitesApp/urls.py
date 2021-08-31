from django.urls import path,include
from tramitesApp.views import listaralumno, agregaralumno,editaralumno,eliminaralumno
from django.contrib.auth import views

urlpatterns = [ 
    path('listaralumno/',listaralumno ,name="listaralumno"),
    path('agregaralumno/',agregaralumno, name="agregaralumno"),
    path('editaralumno/<int:id>/',editaralumno, name="editaralumno"),
    path('eliminaralumno/<int:id>/',eliminaralumno, name="eliminaralumno"),    
]