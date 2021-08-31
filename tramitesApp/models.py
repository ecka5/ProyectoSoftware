from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    codigo=models.CharField(max_length=10)   
    dni=models.CharField(max_length=8)
    direccion=models.CharField(max_length=80)
    email=models.EmailField()
    telefono=models.CharField(max_length=9)
    estado=models.BooleanField()
    def __str__(self):
        return self.nombres

class TipoTramite(models.Model):
    tipoTramite=models.CharField(max_length=50)
    estado=models.BooleanField()
    def __str__(self):
        return self.tipoTramite

class Tramite(models.Model):
    tipoTramite=models.ForeignKey(TipoTramite,on_delete=models.CASCADE)
    alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE)
    estado=models.BooleanField(default=True)
    firma=models.ImageField(upload_to="tramite",null=True)
    def __str__(self):
        return self.firma