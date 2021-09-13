from django.db import models
from django.contrib.auth.models import User
import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Alumno(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    codigo=models.CharField(max_length=10)   
    dni=models.CharField(max_length=8)
    direccion=models.CharField(max_length=80)
    email=models.EmailField()
    telefono=models.CharField(max_length=9)
    facultad=models.CharField(default="INGENIERIA",max_length=10)
    escuela=models.CharField(default="INGENIERIA DE SISTEMAS",max_length=22)
    firma=models.ImageField(upload_to="alumno",null = True)
    estado=models.BooleanField()    
    def __str__(self):
        return self.nombres

class TipoTramite(models.Model):
    abreviatura_tipoTramite=models.CharField(max_length=8)
    tipoTramite=models.CharField(max_length=90)
    estado=models.BooleanField()
    def __str__(self):
        return self.tipoTramite
    
class Requisito(models.Model):
    abreviatura_req=models.CharField(max_length=12)
    tipoTramite=models.ForeignKey(TipoTramite,on_delete=models.CASCADE, null = True)
    requisito=models.CharField(max_length=200)    
    estado=models.BooleanField()
    def __str__(self):
        return self.requisito

class File_tramite(models.Model):    
    requisito1=models.FileField(upload_to="tramite/",null = True)
    requisito2=models.FileField(upload_to="tramite/",null = True)
    requisito3=models.FileField(upload_to="tramite/",null = True)
    requisito4=models.FileField(upload_to="tramite/",null = True)
    requisito5=models.FileField(upload_to="tramite/",null = True)
    requisito6=models.FileField(upload_to="tramite/",null = True)
    requisito7=models.FileField(upload_to="tramite/",null = True)
    requisito8=models.FileField(upload_to="tramite/",null = True)    

class Tramite(models.Model):
    tipoTramite=models.ForeignKey(TipoTramite,on_delete=models.CASCADE)
    alumnos=models.ForeignKey(Alumno,on_delete=models.CASCADE)
    fechatram = models.DateField(default=datetime.date.today,editable=False)
    estado=models.CharField(max_length=20, default="CREADO")
    file_tramite=models.ForeignKey(File_tramite,on_delete=models.CASCADE)

def save(self, *args, **kwargs):
        print('save() is called.')
        super(File_tramite, self).save(*args, **kwargs)

@receiver(pre_save, sender=File_tramite)
@receiver(post_save, sender=File_tramite)
def reicever(*args, **kwargs):
    print('signal dispatched')

class Fut(models.Model):
    tipoTramite=models.ForeignKey(TipoTramite,on_delete=models.CASCADE)
    alumnos=models.ForeignKey(Alumno,on_delete=models.CASCADE)
    objeto=models.CharField(max_length=500,null = True)
    fecha = models.DateField(default=datetime.date.today,editable=False) 
    estado=models.BooleanField(default=True,editable=False)
