from django.urls import path,include
from tramitesApp.views import listaralumno, agregaralumno,editaralumno,eliminaralumno,vistaalumno
from django.contrib.auth import views

urlpatterns = [ 
    path('listaralumno/',listaralumno ,name="listaralumno"),
    path('agregaralumno/',agregaralumno, name="agregaralumno"),
    path('editaralumno/<int:id>/',editaralumno, name="editaralumno"),
    path('eliminaralumno/<int:id>/',eliminaralumno, name="eliminaralumno"),        
    path('vistaalumno/<int:id>/',vistaalumno, name="vistaalumno"),    
    # path('vista/<int:id>/',vista.as_view(), name="vista"),

]