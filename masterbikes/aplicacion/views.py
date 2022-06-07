import code
from django.shortcuts import get_object_or_404, redirect, render
from aplicacion.models import Bicicleta
from aplicacion.form import frmBicicleta

# Create your views here.
def mantencion(request):
    people=Bicicleta.objects.all()
    total=Bicicleta.objects.count()
    contexto={
        "mantenciones":people,
        "total":total
    }
    return render(request,"aplicacion/mantencion.html",contexto)

def home(request):

    return render(request,'aplicacion/home.html')

def crear(request):
    formulario=frmBicicleta(request.POST or None)
    contexto={
        "frm":frmBicicleta
    }

    if request.method=="POST":
        formulario=frmBicicleta(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="mantencion")
    return render(request,"aplicacion/crear.html",contexto)

def modificar(request,id):
    bicicleta=get_object_or_404(Bicicleta,code=id)
    frm=frmBicicleta(instance=bicicleta)
    
    contexto={
        "frm":frm
    }
    if request.method=="POST":
        frm=frmBicicleta(data=request.POST,instance=bicicleta)
        if frm.is_valid():
            bicicleta_mod=Bicicleta.objects.get(code=bicicleta.code)
            datos=frm.cleaned_data
            bicicleta_mod.duenio=datos.get("duenio")
            bicicleta_mod.tecnico=datos.get("tecnico")
            bicicleta_mod.marca=datos.get("marca")
            bicicleta_mod.modelo=datos.get("modelo")
            bicicleta_mod.tiempo=datos.get("tiempo")
            bicicleta_mod.llegada=datos.get("llegada")
            bicicleta_mod.entrega=datos.get("entrega")
            bicicleta_mod.save()
            return redirect(to="mantencion")
            
        
    return render(request,"aplicacion/modificar.html",contexto)

def eliminar(request,id):
    mantencion_tokill=get_object_or_404(Bicicleta,code=id)
    
    contexto={
        "mantenciones":mantencion_tokill
    }
    if request.method=="POST":
        mantencion_tokill.delete()
        return redirect(to="mantencion")
    
    return render(request,"aplicacion/eliminar.html",contexto)
    rut