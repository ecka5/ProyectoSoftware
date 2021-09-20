from django.contrib import admin
from tramitesApp.models import Alumno,Requisito,TipoTramite,Tramite,Fut

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
     list_display=("nombres","apellidos","codigo","dni", "direccion","email","telefono","facultad","escuela","firma","imgperfil")
admin.site.register(Alumno,AlumnoAdmin)

class TipoTramiteAdmin(admin.ModelAdmin):
     list_display=['tipoTramite']
admin.site.register(TipoTramite,TipoTramiteAdmin)

class RequisitoAdmin(admin.ModelAdmin):
     list_display=("tipoTramite","requisito")
admin.site.register(Requisito,RequisitoAdmin)

class TramiteAdmin(admin.ModelAdmin):
     list_display=("tipoTramite","alumnos","fechatram")
admin.site.register(Tramite,TramiteAdmin)

class FutAdmin(admin.ModelAdmin):
     list_display=("alumnos","tipoTramite","objeto")
admin.site.register(Fut,FutAdmin)