from django import forms
from django.forms import fields
from .models import Alumno,Requisito,TipoTramite,Tramite,Fut

class AlumnoForm(forms.ModelForm): 
    class Meta:
        model=Alumno
        fields='__all__'

class TipoTramiteForm(forms.ModelForm): 
    class Meta:
        model=TipoTramite
        fields='__all__'
        
class RequisitoForm(forms.ModelForm): 
    class Meta:
        model=Requisito
        fields='__all__'

class TramiteForm(forms.ModelForm): 
    class Meta:
        model=Tramite
        fields=['tipoTramite','alumnos','estado','file_tramite']

class FutForm(forms.ModelForm): 
    class Meta:
        model=Fut
        fields=['tipoTramite','objeto']