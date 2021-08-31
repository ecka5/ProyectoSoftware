from django.contrib import admin
from tramitesApp.models import Alumno,TipoTramite,Tramite

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
     list_display=("nombres","apellidos","codigo","dni", "direccion","email","telefono")
admin.site.register(Alumno,AlumnoAdmin)

class TipoTramiteAdmin(admin.ModelAdmin):
     list_display=("tipoTramite")
admin.site.register(TipoTramite)

class TramiteAdmin(admin.ModelAdmin):
     list_display=("tipoTramite","firma")
admin.site.register(Tramite,TramiteAdmin)