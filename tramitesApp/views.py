from django.shortcuts import render,redirect
from tramitesApp.models import Alumno, TipoTramite, Tramite,Requisito
from django.db.models import Q
from .forms import AlumnoForm,TipoTramiteForm,RequisitoForm
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.http.response import HttpResponse, JsonResponse
# Create your views here.

def listaralumno(request):
    queryset=request.GET.get("buscar")
    alumno=Alumno.objects.filter(estado=True)
    # paginación
    paginator = Paginator(alumno,3)
    pagina = request.GET.get("page") or 1
    alumno = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1,alumno.paginator.num_pages +1)
    if queryset:
        alumno=Alumno.objects.filter(
            Q(descripcion__icontains=queryset),estado=True
        ).distinct()
    # tb agregaremos la paginación
    context={'alumno':alumno,'pagina':pagina,'paginas':paginas,'pagina_actual':pagina_actual} #pasa de la variable al dicciionario

    return render(request,"alumno/listaralumno.html",context)

def agregaralumno(request):
    form=AlumnoForm()
    if request.method=="POST":
        form=AlumnoForm(request.POST)
        if form.is_valid():
            form.estado=True
            form.save()
            return redirect("listaralumno")
    context={'form':form}
    return render(request,"alumno/agregaralumno.html",context)

def editaralumno(request,id):
    alumno=Alumno.objects.get(id=id)
    if request.method=="POST":
        form=AlumnoForm(request.POST,instance=alumno)
        if form.is_valid():
            form.save()
            return redirect("listaralumno")
    else:
        form=AlumnoForm(instance=alumno)
    context={"form":form}
    return render(request,"alumno/editaralumno.html",context)

def vistaalumno(request,id):
    alumno=Alumno.objects.get(id=id)
    form=AlumnoForm(instance=alumno)
    context={"form":form}
    return render(request,"alumno/vistaalumno.html",context)

# class vista(TemplateView):
#     def get(self,request,*args,**kwargs):
#         alumno=Alumno.objects.get(id=id)
#         form=AlumnoForm(instance=alumno)
#         context={"form":form}
#         return render(request,"alumno/vistaalumno.html",context)

def eliminaralumno(request,id):
    alumno=Alumno.objects.get(id=id)
    alumno.estado=False
    alumno.save()
    return redirect("listaralumno")

# TIPOS DE TRÁMITES

def listartipostramites(request):
    queryset=request.GET.get("buscar")
    tipoT=TipoTramite.objects.filter(estado=True)
    requisito=Requisito.objects.filter(estado=True).distinct
    # paginación
    paginator = Paginator(tipoT,4)
    pagina = request.GET.get("page") or 1
    tipoT = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1,tipoT.paginator.num_pages +1)
    if queryset:
        tipoT=TipoTramite.objects.filter(
            Q(tipoTramite__icontains=queryset),estado=True
        ).distinct()
    # tb agregaremos la paginación
    context={'tipoT':tipoT,'requisito':requisito,'pagina':pagina,'paginas':paginas,'pagina_actual':pagina_actual} #pasa de la variable al dicciionario

    return render(request,"tipotramite/listartipostramites.html",context)

def agregartipostramites(request):
    form=TipoTramiteForm()
    if request.method=="POST":
        form=TipoTramiteForm(request.POST)
        if form.is_valid():
            form.estado=True
            form.save()
            return redirect("listartipostramites")
    context={'form':form}
    return render(request,"tipotramite/agregartipostramites.html",context)


def editartipostramites(request,id):
    tipoT=TipoTramite.objects.get(id=id)
    if request.method=="POST":
        form=TipoTramiteForm(request.POST,instance=tipoT)
        if form.is_valid():
            form.save()
            return redirect("listartipostramites")
    else:
        form=TipoTramiteForm(instance=tipoT)
    context={"form":form}
    return render(request,"tipotramite/editartipostramites.html",context)


def eliminartipostramites(request,id):
    tipoT=TipoTramite.objects.get(id=id)
    tipoT.estado=False
    tipoT.save()
    return redirect("listartipostramites")

# REQUISITOS
def listarrequisitos(request):
    queryset=request.GET.get("buscar")
    requisito=Requisito.objects.filter(estado=True)
    tipoT=TipoTramite.objects.filter(estado=True).distinct
    # paginación
    paginator = Paginator(requisito,4)
    pagina = request.GET.get("page") or 1
    requisito = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1,requisito.paginator.num_pages +1)
    if queryset:
        requisito=Requisito.objects.filter(
            Q(requisito__icontains=queryset),estado=True
        ).distinct()
    # tb agregaremos la paginación
    context={'requisito':requisito,'tipoT':tipoT,'pagina':pagina,'paginas':paginas,'pagina_actual':pagina_actual} 

    return render(request,"requisito/listarrequisitos.html",context)

def agregarrequisitos(request):
    form=RequisitoForm()
    if request.method=="POST":
        form=RequisitoForm(request.POST)
        if form.is_valid():
            form.estado=True
            form.save()
            return redirect("listarrequisitos")
    context={'form':form}
    return render(request,"requisito/agregarrequisitos.html",context)

def mostrarrequisitos(request,id):
    data = Requisito.objects.filter(tipoTramite_id=id).distinct
    context={'data':data}    
    return render(request,"requisito/mostrarrequisitos.html",context)
    

