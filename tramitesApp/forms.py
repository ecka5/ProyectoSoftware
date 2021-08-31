from django import forms
from django.forms import fields
from .models import Alumno,TipoTramite,Tramite

class AlumnoForm(forms.ModelForm): 
    class Meta:
        model=Alumno
        fields='__all__'

class TipoTramiteForm(forms.ModelForm): 
    class Meta:
        model=TipoTramite
        fields='__all__'

class TramiteForm(forms.ModelForm): 
    class Meta:
        model=Tramite
        fields='__all__'