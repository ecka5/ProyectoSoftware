from django.urls import path,include
from tramitesApp.views import listaralumno, agregaralumno,editaralumno,eliminaralumno,listartipostramites,agregartipostramites,editartipostramites,eliminartipostramites
from django.contrib.auth import views

urlpatterns = [ 
    path('listaralumno/',listaralumno ,name="listaralumno"),
    path('agregaralumno/',agregaralumno, name="agregaralumno"),
    path('editaralumno/<int:id>/',editaralumno, name="editaralumno"),
    path('eliminaralumno/<int:id>/',eliminaralumno, name="eliminaralumno"),    
    path('listartipostramites/',listartipostramites ,name="listartipostramites"),
    path('agregartipostramites/',agregartipostramites, name="agregartipostramites"),
    path('editartipostramites/<int:id>/',editartipostramites, name="editartipostramites"),
    path('eliminartipostramites/<int:id>/',eliminartipostramites, name="eliminartipostramites"),    
]