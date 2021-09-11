from django.contrib import admin
from tramitesApp.models import Alumno,Requisito,TipoTramite,Tramite,EstadoTramite,BandejaTramite,Fut

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
     list_display=("nombres","apellidos","codigo","dni", "direccion","email","telefono","facultad","escuela","firma")
admin.site.register(Alumno,AlumnoAdmin)

class TipoTramiteAdmin(admin.ModelAdmin):
     list_display=['tipoTramite']
admin.site.register(TipoTramite,TipoTramiteAdmin)

class RequisitoAdmin(admin.ModelAdmin):
     list_display=("tipoTramite","requisito")
admin.site.register(Requisito,RequisitoAdmin)

class TramiteAdmin(admin.ModelAdmin):
     list_display=("tipoTramite","alumnos","fechatram","archivo")
admin.site.register(Tramite,TramiteAdmin)

class EstadoTramiteAdmin(admin.ModelAdmin):
     list_display=['estadotram']
admin.site.register(EstadoTramite,EstadoTramiteAdmin)

class BandejaTramiteAdmin(admin.ModelAdmin):
     list_display=("tramites","estadotramites","observacion","tiempo","fechabandeja")
admin.site.register(BandejaTramite,BandejaTramiteAdmin)

class FutAdmin(admin.ModelAdmin):
     list_display=("alumnos","tipoTramite")
admin.site.register(Fut,FutAdmin)