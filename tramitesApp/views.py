from django.shortcuts import render,redirect
from tramitesApp.models import Alumno, TipoTramite, Tramite,Requisito,Fut,File_tramite, save
from django.db.models import Q
from .forms import AlumnoForm,TipoTramiteForm,RequisitoForm,FutForm, TramiteForm
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.http.response import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.urls import reverse

#PDF{
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
#} TERMINA PDF

#ALUMNOS
def listaralumno(request):    
    if request.user.is_staff:
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
    else:        
        queryset=request.GET.get("buscar")
        alumno=Alumno.objects.filter(user=request.user)         
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
    if request.method=="POST":
        form=AlumnoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.estado=True
            form.save()
            return redirect("listaralumno")
    else:
        form=AlumnoForm()
    context={'form':form}
    return render(request,"alumno/agregaralumno.html",context)

def editaralumno(request,id):
    alumno=Alumno.objects.get(id=id)
    if request.method=="POST":
        form=AlumnoForm(request.POST,instance=alumno,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("perfilalumno")
    else:
        form=AlumnoForm(instance=alumno)
    context={"form":form}
    return render(request,"alumno/editaralumno.html",context)

def vistaalumno(request,id):
    alumno=Alumno.objects.get(id=id)
    form=AlumnoForm(instance=alumno)
    context={"form":form}
    return render(request,"alumno/vistaalumno.html",context)

def eliminaralumno(request,id):
    alumno=Alumno.objects.get(id=id)
    alumno.estado=False
    alumno.save()
    return redirect("listaralumno")

#PERFIL

def perfilalumno(request):    
    if request.user.is_staff:
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
        
        return render(request,"alumno/perfilalumno.html",context)        
    else:        
        queryset=request.GET.get("buscar")
        alumno=Alumno.objects.filter(user=request.user)         
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

        return render(request,"alumno/perfilalumno.html",context)


# TIPOS DE TRÁMITES

def listartipostramites(request):
    queryset=request.GET.get("buscar")
    tipoT=TipoTramite.objects.filter(estado=True)
    requisito=Requisito.objects.filter(estado=True).distinct
    # paginación
    paginator = Paginator(tipoT,8)
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
    paginator = Paginator(requisito,8)
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
    
#FUTS

def listarfuts(request):
    username=request.user 
    queryset=request.GET.get("buscar")
    alumno = Alumno.objects.get(user=username)
    fut=Fut.objects.filter(estado=True,alumnos=alumno)
    # paginación
    paginator = Paginator(fut,4)
    pagina = request.GET.get("page") or 1
    fut = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1,fut.paginator.num_pages +1)
    if queryset:
        fut=Fut.objects.filter(
            Q(fut__icontains=queryset),estado=True
        ).distinct()
    # tb agregaremos la paginación
    context={'fut':fut,'pagina':pagina,'paginas':paginas,'pagina_actual':pagina_actual} #pasa de la variable al dicciionario

    return render(request,"fut/listarfuts.html",context)


def agregarfuts(request):
    form=FutForm()
    username=request.user
    if request.method=="POST":
        form=FutForm(request.POST)
        if form.is_valid():
            formAlum = form.save(commit=False)
            alumno = Alumno.objects.get(user=username)
            formAlum.alumnos = alumno
            formAlum.estado=True
            formAlum.save()
            return redirect("listarfuts")
    context={'form':form}
    return render(request,"fut/agregarfuts.html",context)

#FUT PDF
def reportfut(request,id):
    data = Fut.objects.filter(id=id).distinct
    context = {'data':data}
    html = render_to_string("report/reportfut.html",context)

    response=HttpResponse(content_type="application/pdf")
    response["Content-Disposition"]="inline;report.pdf"

    font_config=FontConfiguration()
    HTML(string=html).write_pdf(response,font_config=font_config)
    return response


#TRÁMITES

def listartramites(request):
    username=request.user 
    queryset=request.GET.get("buscar")
    alumno = Alumno.objects.get(user=username)
    tramites=Tramite.objects.filter(alumnos=alumno)
    tipoTramite=TipoTramite.objects.filter(estado=True)
    requisito=Requisito.objects.filter(estado=True).distinct
    # paginación
    paginator = Paginator(tramites,2)
    pagina = request.GET.get("page") or 1
    tramites = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1,tramites.paginator.num_pages +1)
    if queryset:
        tramites=Tramite.objects.filter(
            Q(tipoTramite__tipoTramite__icontains=queryset),estado=True
        ).distinct()
    # tb agregaremos la paginación
    context={'tipoTramite':tipoTramite,'tramites':tramites,'requisito':requisito,'pagina':pagina,'paginas':paginas,'pagina_actual':pagina_actual} #pasa de la variable al dicciionario
    return render(request,"tramite/listartramites.html",context)

def agregartramites(request): 
    form=TramiteForm()
    username=request.user 
    if request.method=="POST":
        form=TramiteForm(request.POST,files=request.FILES)
        if form.is_valid():          
            formAlum = form.save(commit=False)
            alumno = Alumno.objects.get(user=username)
            formAlum.alumnos = alumno
            formAlum.estado=True
            formAlum.save()
            return redirect("listartramites")
    context={'form':form}
    return render(request,"tramite/agregartramites.html",context)

def editartramites(request,id):
    tramite=Tramite.objects.get(id=id)
    if request.method=="POST":
        form=TramiteForm(request.POST,instance=tramite,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listartramites")
    else:
        form=TramiteForm(instance=tramite)
    context={"form":form}
    return render(request,"tramite/editartramites.html",context)

def requisitostramite(request,id):
    data = Requisito.objects.filter(tipoTramite_id=id).distinct
    context={'data':data}    
    return context

def modelodoc(request):   
    return render(request,"requisito/modelodoc.html")

def tipoTramite(request):
    if request.method=="POST":
        tipo=request.POST['abreviatura_tipoTramite']
        tipo_get=TipoTramite.objects.get(abreviatura_tipoTramite=tipo)
        req=Requisito.objects.filter(tipoTramite=tipo_get)
        if tipo=="RM":
            context={'tipo':tipo_get,'req1': req[0],'req2':req[1],'req3':req[2]}
            return render(request,"tramites_tipo/3requisitos.html",context)
        if tipo=="MC" or tipo=="ACCC" or tipo =="ACPP" or tipo=="TCV": 
            context={'tipo':tipo_get,'req1': req[0],'req2':req[1],'req3':req[2],'req4':req[3]}
            return render(request,"tramites_tipo/4requisitos.html",context)            
        if tipo=="ES":
            context={'tipo':tipo_get,'req1': req[0],'req2':req[1],'req3':req[2],'req4':req[3],'req5':req[4],'req6':req[5]}
            return render(request,"tramites_tipo/6requisitos.html",context)        
        if tipo=="TOG":
            context={'tipo':tipo_get,'req1': req[0],'req2':req[1],'req3':req[2],'req4':req[3],'req5':req[4]}
            return render(request,"tramites_tipo/5requisitos.html",context)
        if tipo=="TOT":
            context={'tipo':tipo_get,'req1': req[0],'req2':req[1],'req3':req[2],'req4':req[3],'req5':req[4],'req6':req[5],'req7':req[6],'req8':req[7]}
            return render(request,"tramites_tipo/8requisitos.html",context) 
    else:
        return redirect(reverse('listartramites'))
    return redirect(reverse('listartramites'))

def savetramite(request):
    if request.method=="POST":
        tipo=request.POST['abreviatura_tipoTramite']
        # fecha=request.POST['fecha_tramite']
        tipo_get=TipoTramite.objects.get(abreviatura_tipoTramite=tipo)
        username=request.user
        alumno = Alumno.objects.get(user=username)
        new_FileTramite=File_tramite()
        if tipo=="RM":
            new_FileTramite.requisito1=request.FILES['id_requisito1']
            new_FileTramite.requisito2=request.FILES['id_requisito2']
            new_FileTramite.requisito3=request.FILES['id_requisito3']
            new_FileTramite.save()
        if tipo=="MC" or tipo=="ACPP" or tipo=="ACCC" or tipo=="TCV":
            new_FileTramite.requisito1=request.FILES['id_requisito1']
            new_FileTramite.requisito2=request.FILES['id_requisito2']
            new_FileTramite.requisito3=request.FILES['id_requisito3']
            new_FileTramite.requisito4=request.FILES['id_requisito4']
            new_FileTramite.save()         
        if tipo=="ES":
            new_FileTramite.requisito1=request.FILES['id_requisito1']
            new_FileTramite.requisito2=request.FILES['id_requisito2']
            new_FileTramite.requisito3=request.FILES['id_requisito3']
            new_FileTramite.requisito4=request.FILES['id_requisito4']
            new_FileTramite.requisito5=request.FILES['id_requisito5']
            new_FileTramite.requisito6=request.FILES['id_requisito6']
            new_FileTramite.save()
        if tipo=="TOG":
            new_FileTramite.requisito1=request.FILES['id_requisito1']
            new_FileTramite.requisito2=request.FILES['id_requisito2']
            new_FileTramite.requisito3=request.FILES['id_requisito3']
            new_FileTramite.requisito4=request.FILES['id_requisito4']
            new_FileTramite.requisito5=request.FILES['id_requisito5']
            new_FileTramite.save()
        if tipo=="TOT":
            new_FileTramite.requisito1=request.FILES['id_requisito1']
            new_FileTramite.requisito2=request.FILES['id_requisito2']
            new_FileTramite.requisito3=request.FILES['id_requisito3']
            new_FileTramite.requisito4=request.FILES['id_requisito4']
            new_FileTramite.requisito5=request.FILES['id_requisito5']
            new_FileTramite.requisito6=request.FILES['id_requisito6']
            new_FileTramite.requisito7=request.FILES['id_requisito7']
            new_FileTramite.requisito8=request.FILES['id_requisito8']
            new_FileTramite.save()
        # completar con mas ifs con cada requisito
        new_Tramite=Tramite()
        new_Tramite.tipoTramite= tipo_get
        new_Tramite.alumnos= alumno
        # new_Tramite.fechatram=fecha 
        new_Tramite.file_tramite=new_FileTramite
        new_Tramite.save()
        return redirect(reverse('listartramites'))
    else:
        return redirect(reverse('listartramites'))

def nuevotramite(request):
    username=request.user 
    queryset=request.GET.get("buscar")
    alumno = Alumno.objects.get(user=username)
    tramites=Tramite.objects.filter(alumnos=alumno)
    tipoTramite=TipoTramite.objects.filter(estado=True)
    requisito=Requisito.objects.filter(estado=True).distinct
    # paginación
    paginator = Paginator(tramites,3)
    pagina = request.GET.get("page") or 1
    tramites = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1,tramites.paginator.num_pages +1)
    if queryset:
        tramites=Tramite.objects.filter(
            Q(tipoTramite__icontains=queryset),estado=True
        ).distinct()
    # tb agregaremos la paginación
    context={'tipoTramite':tipoTramite,'tramites':tramites,'requisito':requisito,'pagina':pagina,'paginas':paginas,'pagina_actual':pagina_actual} #pasa de la variable al dicciionario
    return render(request,"tramite/nuevotramite.html",context)
# secretaria
def secre(request):
    tramites=Tramite.objects.filter()
    context={'tramites':tramites}  
    return render(request,"secretaria/index.html",context)

def verificado(request,id):
    Tramite.objects.filter(id=id).update(estado="VERIFICADO")
    return redirect(reverse('secre'))

def rechazado(request,id):
    Tramite.objects.filter(id=id).update(estado="RECHAZADO")
    return redirect(reverse('secre'))

# director
def direc(request):
    tramites=Tramite.objects.filter()
    context={'tramites':tramites}  
    return render(request,"director/index.html",context)

def visadod(request,id):
    Tramite.objects.filter(id=id).update(estado="VISADO")
    return redirect(reverse('direc'))

def rechazadod(request,id):
    Tramite.objects.filter(id=id).update(estado="RECHAZADO")
    return redirect(reverse('direc'))