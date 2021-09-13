from django.urls import path,include
from tramitesApp.views import listaralumno, agregaralumno,editaralumno,eliminaralumno
from tramitesApp.views import listartipostramites,agregartipostramites,editartipostramites,eliminartipostramites,nuevotramite
from tramitesApp.views import listarrequisitos,mostrarrequisitos,agregarrequisitos,listartramites
from tramitesApp.views import agregarfuts,agregartramites,requisitostramite,editartramites
from tramitesApp.views import modelodoc,listarfuts,tipoTramite,savetramite,secre,verificado,rechazado,direc,visadod,rechazadod,reportfut
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
    path('nuevotramite/',nuevotramite, name="nuevotramite"),
    
    #FUTS
    path('listarfuts/',listarfuts ,name="listarfuts"),
    path('agregarfuts/',agregarfuts, name="agregarfuts"),
    
    #MODAL MODELO DE DOCUMENTOS 
    path('modelodoc/',modelodoc, name="modelodoc"),

     #MODAL new tramite
    path('tipoTramite/',tipoTramite, name="tipoTramite"),

    #GUARDAR EL TRAMITE
    path('savetramite/',savetramite, name="savetramite"),

    #secre
    path('secre/',secre,name="secre"),
    path('rechazado/<int:id>/',rechazado,name="rechazado"),
    path('verificado/<int:id>/',verificado,name="verificado"),

    # sdirec
    path('direc/',direc,name="direc"),
    path('rechazadod/<int:id>/',rechazadod,name="rechazadod"),
    path('visadod/<int:id>/',visadod,name="visadod"),
    
    #REPORT FUT
    path('reportfut/<int:id>/',reportfut,name="reportfut"),

]    
