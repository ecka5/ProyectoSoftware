from django.urls import path,include
from tramitesApp.views import listaralumno, agregaralumno,editaralumno,eliminaralumno,listartipostramites,agregartipostramites,editartipostramites,eliminartipostramites,listarrequisitos,mostrarrequisitos,agregarrequisitos,listartramites,agregarfuts,agregartramites,requisitostramite,editartramites,modelodoc,listarfuts
from django.contrib.auth import views

urlpatterns = [ 
    
    #ALUMNOS
    path('listaralumno/',listaralumno ,name="listaralumno"),
    path('agregaralumno/',agregaralumno, name="agregaralumno"),
    path('editaralumno/<int:id>/',editaralumno, name="editaralumno"),
    path('eliminaralumno/<int:id>/',eliminaralumno, name="eliminaralumno"),    
    #TIPOS DE TRÁMITES
    path('listartipostramites/',listartipostramites ,name="listartipostramites"),
    path('agregartipostramites/',agregartipostramites, name="agregartipostramites"),
    path('editartipostramites/<int:id>/',editartipostramites, name="editartipostramites"),
    path('eliminartipostramites/<int:id>/',eliminartipostramites, name="eliminartipostramites"),    
    
    #REQUISITOS
    path('listarrequisitos/',listarrequisitos ,name="listarrequisitos"), 
    path('agregarrequisitos/',agregarrequisitos, name="agregarrequisitos"),
    path('mostrarrequisitos/<int:id>/',mostrarrequisitos ,name="mostrarrequisitos"), 

    #TRAMITES
    path('listartramites/',listartramites, name="listartramites"),
    path('agregartramites/',agregartramites, name="agregartramites"),
    path('editartramites/<int:id>/',editartramites, name="editartramites"),
    path('requisitostramite/<int:id>/',requisitostramite, name="requisitostramite"),
    #FUTS
    path('listarfuts/',listarfuts ,name="listarfuts"),
    path('agregarfuts/',agregarfuts, name="agregarfuts"),
    
    #MODAL MODELO DE DOCUMENTOS 
    path('modelodoc/',modelodoc, name="modelodoc"),
    
]