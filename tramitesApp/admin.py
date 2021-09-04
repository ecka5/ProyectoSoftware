from django.contrib import admin
from tramitesApp.models import Alumno,Requisito,TipoRequisito,TipoTramite,Tramite,EstadoTramite,BandejaTramite

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
     list_display=("nombres","apellidos","codigo","dni", "direccion","email","telefono","facultad","escuela","firma")
admin.site.register(Alumno,AlumnoAdmin)

class TipoTramiteAdmin(admin.ModelAdmin):
     list_display=['tipoTramite']
admin.site.register(TipoTramite,TipoTramiteAdmin)

class TipoRequisitoAdmin(admin.ModelAdmin):
     list_display=("tipoRequisito","tipoTramites")
admin.site.register(TipoRequisito,TipoRequisitoAdmin)

class RequisitoAdmin(admin.ModelAdmin):
     list_display=("requisito","archivo","tipoRequisitos")
admin.site.register(Requisito,RequisitoAdmin)

class TramiteAdmin(admin.ModelAdmin):
     list_display=("tipoTramite","alumnos")
admin.site.register(Tramite,TramiteAdmin)

class EstadoTramiteAdmin(admin.ModelAdmin):
     list_display=['estadotram']
admin.site.register(EstadoTramite,EstadoTramiteAdmin)

class BandejaTramiteAdmin(admin.ModelAdmin):
     list_display=("tramites","estadotramites","observacion","tiempo","fecha")
admin.site.register(BandejaTramite,BandejaTramiteAdmin)