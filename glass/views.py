from django.shortcuts import render, get_object_or_404 
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from models import *
from forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    visi = Visitas.objects.get(id='2')
    
    visi.home = visi.home + 1
    visi.save()
    
    titulo = "Master AutoGlass"
    template = "home.html"
    slider = Slide.objects.all()
    ban = Mensajeb.objects.all()
    
    for b in ban:
        if b.valida:
           ba = b
    
    primera =""
    segunda = ""
    tercera = ""
    contador = 0 
    
    for s in slider:
        if s.valida:
            
            if s.orden.orden == "Tercero":
                tercera = s
                contador+=1
            if s.orden.orden == "Segundo":
                segunda = s
                contador+=1
            if s.orden.orden == "Primero":
                primera = s
                contador+=1
      
    return render_to_response(template,context_instance=RequestContext(request,locals()))


def servicios(request):
    visi = Visitas.objects.get(id='2')
    
    visi.servi = visi.servi + 1
    visi.save()
    servi =[]
   
    ser = Servicios.objects.all()
    for s in ser:
        if s.valida:
            servi.append(s)
    
    titulo = "SERVICIOS"
    template = 'servicios.html'
    return render_to_response(template,context_instance=RequestContext(request,locals()))


def detalleservice(request, idser):
    servicio = get_object_or_404(Servicios, pk=idser)
    
    if not servicio.valida:
        ser = Servicios.objects.all()
        fl = True
        for se in ser:
            if se.valida:
                servicio = se
                break
                      
    titulo = servicio.titulo
    template = 'servi2.html'
    return render_to_response(template,context_instance=RequestContext(request,locals()))
        
        
        
    
   
        
    
   


def contacto(request):
    visi = Visitas.objects.get(id='2')
    
    visi.contacto = visi.contacto + 1
    visi.save()
    
    titulo = "Contactenos"
    template = 'contacto.html'
    return render_to_response(template,context_instance=RequestContext(request,locals()))
    
    
def fotos(request):
    visi = Visitas.objects.get(id='2')
    
    visi.fotos = visi.fotos + 1
    visi.save()
    
    titulo = "Galeria de fots"
    template = "fotos.html"
    fota = Fotos.objects.all()
    fot = []
    
    for f in fota:
        if f.valida:
            fot.append(f)
    
       
    return render_to_response(template,context_instance=RequestContext(request,locals()))
    
    
def quienes(request):
    titulo = "Quienes somos"
    c = {'titulo': titulo}
    return render_to_response('quienes.html',c)



def ubicacion(request):
    visi = Visitas.objects.get(id='2')
    
    visi.mapa = visi.mapa + 1
    visi.save()
    
    titulo = "Nuestra Ubicacion"
    template = 'ubicacion.html'
    return render_to_response(template,context_instance=RequestContext(request,locals()))

    
def login(request):
    titulo = "Login"
    c = {'titulo': titulo}
    return render_to_response('login.html',c)
    
    
@login_required
def conf(request):
    if request.POST:
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/conf")
    else:
        form = SlideForm()
        sl = Slide.objects.all()
        
    template = "cofiguraciones.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required
def cfotos(request):
    if request.POST:
        formf = FotosForm(request.POST, request.FILES)
        if formf.is_valid():
            formf.save()
            return HttpResponseRedirect("/cfotos")
    else:
        formf = FotosForm()
        fot = Fotos.objects.all()
        
    template = "confotos.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
 
@login_required  
def cservicios(request):
     if request.POST:
        formser = ServiciosForm(request.POST, request.FILES)
        if formser.is_valid():
            formser.save()
            return HttpResponseRedirect("/cservicios")
     else:
         formser = ServiciosForm()
         servi = Servicios.objects.all()
        
     template = "confservicios.html"
     return render_to_response(template,context_instance=RequestContext(request,locals()))
    
@login_required   
def banner(request):
    if request.POST:
        formb = MensajebForm(request.POST, request.FILES)
        if formb.is_valid():
            formb.save()
            return HttpResponseRedirect("/banner")
    else:
        formb = MensajebForm()
        baner = Mensajeb.objects.all()
        
    template = "confbanner.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required
def info(request):
    titulo = "Login"
    c = {'titulo': titulo}
    return render_to_response('login.html',c)

@login_required
def ccontacto(request):
    titulo = "Login"
    c = {'titulo': titulo}
    return render_to_response('login.html',c)
    
    
    
    
def slideupdate(request, idslide):
    slide = get_object_or_404(Slide, pk=idslide)
    if request.POST:
        formslide = SlideForm(request.POST, request.FILES, instance=slide)
        if formslide.is_valid():
            formslide.save()
            return HttpResponseRedirect("/conf")
    else:
        formslide = SlideForm(instance=slide)
        
    template = "slideupdate.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
   
def eliminarslide(request, idslide):
    slide = get_object_or_404(Slide,pk=idslide)
    if request.POST:
        slide.delete()
        return HttpResponseRedirect("/conf")
        
    template = "eliminarslide.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
            
def editarfoto(request, idfoto):
    foto = get_object_or_404(Fotos, pk=idfoto)
    if request.POST:
        formfoto = FotosForm(request.POST, request.FILES, instance=foto)
        if formfoto.is_valid():
            formfoto.save()
            return HttpResponseRedirect("/cfotos")
    else:
        formfoto = FotosForm(instance=foto)
        
    template = "editarfoto.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
   
def eliminarfoto(request, idfoto):
    foto = get_object_or_404(Fotos,pk=idfoto)
    if request.POST:
        foto.delete()
        return HttpResponseRedirect("/cfotos")
        
    template = "eliminarfoto.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
    
    
    
def editarservicio(request, idservi):
    servi = get_object_or_404(Servicios, pk=idservi)
    if request.POST:
        formservi = ServiciosForm(request.POST, request.FILES, instance=servi)
        if formservi.is_valid():
            formservi.save()
            return HttpResponseRedirect("/cservicios")
    else:
        formservi = ServiciosForm(instance=servi)
        
    template = "editarservicio.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
   
def eliminarserivicio(request, idservi):
    servi = get_object_or_404(Servicios,pk=idservi)
    if request.POST:
        servi.delete()
        return HttpResponseRedirect("/cservicios")
        
    template = "eliminarservicio.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
    
    
    
def editarbanner(request, idbaner):
    ban = get_object_or_404(Mensajeb, pk=idbaner)
    if request.POST:
        formba = MensajebForm(request.POST, request.FILES, instance=ban)
        if formba.is_valid():
            formba.save()
            return HttpResponseRedirect("/banner")
    else:
        formba = MensajebForm(instance=ban)
        
    template = "editarbanner.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
   
def eliminarbanner(request, idbaner):
    ban = get_object_or_404(Mensajeb,pk=idbaner)
    if request.POST:
        ban.delete()
        return HttpResponseRedirect("/banner")
        
    template = "eliminarbanner.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))