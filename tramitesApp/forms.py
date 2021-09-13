from django import forms
from django.forms import fields
from .models import Alumno,Requisito,TipoTramite,Tramite,EstadoTramite,BandejaTramite,Fut

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
        fields=['tipoTramite','archivo']

class EstadoTramiteForm(forms.ModelForm): 
    class Meta:
        model=EstadoTramite
        fields='__all__'
        
class BandejaTramiteForm(forms.ModelForm): 
    class Meta:
        model=BandejaTramite
        fields='__all__'

class FutForm(forms.ModelForm): 
    class Meta:
        model=Fut
        fields=['tipoTramite','objeto']