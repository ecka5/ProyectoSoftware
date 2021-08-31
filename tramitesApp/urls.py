from django.urls import path,include
<<<<<<< HEAD
from tramitesApp.views import listaralumno, agregaralumno,editaralumno,eliminaralumno,vistaalumno
=======
from tramitesApp.views import listaralumno, agregaralumno,editaralumno,eliminaralumno,listartipostramites,agregartipostramites,editartipostramites,eliminartipostramites
>>>>>>> e317d30bfed94f4cbb08139ac353f3149026b008
from django.contrib.auth import views

urlpatterns = [ 
    path('listaralumno/',listaralumno ,name="listaralumno"),
    path('agregaralumno/',agregaralumno, name="agregaralumno"),
    path('editaralumno/<int:id>/',editaralumno, name="editaralumno"),
<<<<<<< HEAD
    path('eliminaralumno/<int:id>/',eliminaralumno, name="eliminaralumno"),        
    path('vistaalumno/<int:id>/',vistaalumno, name="vistaalumno"),    
    # path('vista/<int:id>/',vista.as_view(), name="vista"),

=======
    path('eliminaralumno/<int:id>/',eliminaralumno, name="eliminaralumno"),    
    path('listartipostramites/',listartipostramites ,name="listartipostramites"),
    path('agregartipostramites/',agregartipostramites, name="agregartipostramites"),
    path('editartipostramites/<int:id>/',editartipostramites, name="editartipostramites"),
    path('eliminartipostramites/<int:id>/',eliminartipostramites, name="eliminartipostramites"),    
>>>>>>> e317d30bfed94f4cbb08139ac353f3149026b008
]